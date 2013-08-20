# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models

CARGO_CHOICES = (('0','Fundador'),('1','Colaborador'))

class Equipe(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=1,choices=CARGO_CHOICES)
    funcao = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos')
    publicar = models.BooleanField(default=True)
    data = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural='Equipe'

    def __unicode__(self):
        return self.nome

class Trabalhos(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='sites')
    descricao = models.TextField('Descrição')
    publicar = models.BooleanField(default=True)
    data = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural='Trabalhos'

    def __unicode__(self):
        return self.nome