from django.db import models

from tailor.models import Pessoa


class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    endereco = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)

    def contratos_abertos(self):
        return 3

    def vagas(self):
        return 1

    def __str__(self):
        return self.nome


class Contato(Pessoa):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)  # Cascade is not the best in this case


class EstagioNegociacao(models.Model):
    estagio = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.estagio


class Contrato(models.Model):
    estagio = models.ForeignKey(EstagioNegociacao, on_delete=models.CASCADE, null=True)
    vagas = models.IntegerField(null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)  # Cascade is not the best in this case
    # vagas Como fazer isso ser visível aqui mas não na vaga em si?
    valor = models.FloatField(max_length=10)
    descricao = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.empresa) + ' ' + str(self.vagas) + ' ' + str(self.estagio)
