# -*- coding: utf-8 -*-
from django.contrib import admin
from website.models import *

__author__ = 'Erivanio'

class EquipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nome', 'sobrenome', 'funcao', 'cargo','foto', 'publicar']})
    ]
    list_display = ('nome', 'sobrenome')
    list_filter = ['funcao', 'publicar', 'data', 'cargo']
    search_fields = ['nome', 'sobrenome', 'funcao']

class TrabalhosAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nome', 'foto', 'descricao', 'publicar']})
    ]
    list_display = ('nome', 'descricao')
    list_filter = ['publicar', 'data']
    search_fields = ['nome', 'descricao']

admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Trabalhos, TrabalhosAdmin)