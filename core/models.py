from django.db import models

# Create your models here.

class Aniversariante(models.Model):
    nome = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
