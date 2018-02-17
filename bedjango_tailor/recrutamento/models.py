from django.db import models

from comercial.models import Empresa
from tailor.models import Pessoa


class Vaga(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()

    def candidatos(self):
        return Aplicacao.objects.filter(vaga=self).count()

    def __str__(self):
        return self.titulo + ' na ' + str(self.empresa)

    class Meta:

        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'


class EtapaRecrutamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:

        verbose_name = 'Etapa de Recrutamento'
        verbose_name_plural = 'Etapas de Recrutamento'


class Candidato(Pessoa):
    linkedin = models.URLField(max_length=50, blank=True)
    github = models.URLField(max_length=50, blank=True)

    class Meta:

        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'

    def candidaturas(self):
        return Aplicacao.objects.filter(candidato=self).count()


class Aplicacao(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    etapa = models.ForeignKey(EtapaRecrutamento, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'Aplicação'
        verbose_name_plural = 'Aplicações'
        unique_together = [['vaga', 'candidato']]
