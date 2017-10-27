from django.db import models

from users.models import User


class Pessoa(User):
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    cidade = models.CharField(max_length=20, blank=True)  # criar model

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name
