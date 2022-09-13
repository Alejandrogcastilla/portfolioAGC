from django.db import models
from datetime import datetime


class Mensajes(models.Model):
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    nombre = models.TextField(blank=False)
    email = models.EmailField(blank=False, max_length=254)
    mensaje = models.TextField(blank=True, max_length=4000)

    class Meta:
        ordering = ['fecha']


class Visitas(models.Model):
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    peticion = models.TextField(blank=False)
