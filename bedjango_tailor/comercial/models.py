from django.db import models

from tailor.models import Pessoa


class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    endereco = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)

    def contratos_abertos(self):
        return Contrato.objects.filter(empresa=self).count()

    def vagas(self):
        from recrutamento.models import Vaga
        return Vaga.objects.filter(empresa=self).count()

    def __str__(self):
        return self.nome

    class Meta:

        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class Contato(Pessoa):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    class Meta:

        verbose_name = 'Contato de Empresa'
        verbose_name_plural = 'Contatos de Empresa'


class EtapaNegociacao(models.Model):
    etapa = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.etapa

    class Meta:

        verbose_name = 'Etapa de Negociação'
        verbose_name_plural = 'Etapas de Negociação'


class Contrato(models.Model):
    etapa = models.ForeignKey(EtapaNegociacao, on_delete=models.CASCADE, null=True)
    vagas = models.IntegerField(null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    valor = models.IntegerField()
    descricao = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.empresa) + ' ' + str(self.vagas) + ' ' + str(self.etapa)

    class Meta:

        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
