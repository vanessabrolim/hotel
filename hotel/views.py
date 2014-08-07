#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from models import *
from forms import *
import datetime


def home(request):
    pessoas = Pessoa.objects.all()
    animais = Animal.objects.all()
    estadias = Estadia.objects.all()
    return render(request, 'home.html',
                  {'animais': animais, 'pessoas': pessoas,
                   'estadias': estadias, })


def naoRolou(request):
    return render(request, 'naoRolou.html', {})

# cadastros





# relatorios
def Relatorios(request):
    return render(request, 'relatorios/relatorios.html', {})


def RecDia(request):
    return render(request, 'relatorios/recomendacoesHoje.html', {})


def RecAmanha(request):
    return render(request, 'relatorios/recomendacoesAmanha.html', {})


def RecOntem(request):
    return render(request, 'relatorios/recomendacoesOntem.html', {})


def Hospedados(request):
    return render(request, 'relatorios/hospedados.html', {})


def Livres(request):
    return render(request, 'relatorios/livres.html', {})


def EstadiaAnimal(request):
    return render(request, 'relatorios/estadiaAnimal.html', {})


def EstadiaPessoa(request):
    return render(request, 'relatorios/estadiaPessoa.html', {})

# edicoes


