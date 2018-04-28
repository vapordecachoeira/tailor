from django.db import models

from users.models import User


class Pessoa(models.Model):
    nome = models.TextField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15, null=True, blank=True)
    celular = models.CharField(max_length=15)
    cidade = models.CharField(max_length=20, blank=True)  # criar model

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome
