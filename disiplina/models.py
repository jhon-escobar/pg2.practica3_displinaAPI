from django.db import models


# Create your models here.
class disiplina(models.model):

    nombre = models.CharField(max_length=150)
    foto = models.CharField(max_length=150)


class tipoCompetencia(models.Model):

    nombre = models.CharField(max_length=150)
    detalle = models.CharField(max_length=150)
    estilo = models.CharField(max_length=150)
    distancia = models.CharField(max_length=150)
    tiempo = models.CharField(max_length=150)


class regla(models.Model):

    numero = models.CharField(max_length=150)
    detalle = models.CharField(max_length=150)
    norma_establecida = models.CharField(max_length=150)


class experto(models.Model):

    nombre = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
