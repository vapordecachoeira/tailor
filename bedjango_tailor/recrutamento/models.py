from django.db import models

from comercial.models import Empresa
from tailor.models import Pessoa


class Vaga(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()

    def candidatos(self):
        return 5

    def __str__(self):
        return self.titulo + ' na ' + str(self.empresa)


class EstagioRecrutamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Candidato(Pessoa):
    linkedin = models.URLField(max_length=50, blank=True)
    github = models.URLField(max_length=50, blank=True)

    def candidaturas(self):
        return 2


class Candidatura(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    estagio = models.ForeignKey(EstagioRecrutamento, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
