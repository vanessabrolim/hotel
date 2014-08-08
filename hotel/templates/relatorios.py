#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from models import *
from forms import *


def Relatorios(request):
    return render(request, 'relatorios/relatorios.html', {})


def RecDia(request):
    return render(request, 'relatorios/recomendacoesHoje.html', {})


def RecAmanha(request):
    return render(request, 'relatorios/recomendacoesAmanha.html', {})


def RecOntem(request):
    return render(request, 'relatorios/recomendacoesOntem.html', {})


def Hospedados(request):
    validaEstadia()
    estadias = Estadia.objects.filter(ativa=1)
    for estadia in estadias:
        animal = Animal.objects.filter(id=estadia.animal.id)

    return render(request, 'relatorios/hospedados.html', {})

def validaEstadia():
    es = Estadia.objects.all()
    hj = datetime.datetime.today()
    for e in es:
        if e.data_saida.month <= hj.month:
            if e.data_saida.day <= hj.day:
                if e.data_saida.year <= hj.year:
                    if e.data_saida.hour> hj.hour:
                        e.ativa=0
                        e.save()
def Livres(request):
    return render(request, 'relatorios/livres.html', {})


def EstadiaAnimal(request):
    return render(request, 'relatorios/estadiaAnimal.html', {})


def EstadiaPessoa(request):
    return render(request, 'relatorios/estadiaPessoa.html', {})
