from django.db import models

# Create your models here.
class Restaurantes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    cuisine = models.ForeignKey('cuisine',on_delete=models.PROTECT,related_name='restaurantes')
    working_hours = models.CharField(max_length=100)


    def __str__(self):
        return self.name
class cuisine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name