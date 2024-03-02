from django.db import models

# Create your models here.
class Restaurantes(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    especialidade = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    pass