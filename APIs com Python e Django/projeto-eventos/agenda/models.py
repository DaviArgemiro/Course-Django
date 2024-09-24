from django.db import models
from django.utils.timezone import now

class Categoria(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200, blank=True)
    date = models.DateField(blank=True, null=True)
    participantes = models.IntegerField(default=0)

    def __str__(self):
        return self.nome