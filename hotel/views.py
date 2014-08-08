#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from models import *
from forms import *
import datetime


def register(request):
    '''
        Renderiza página para registro de usuários no sistema
    '''
    erro = None
    user = None
    registered = False
    user_form = UserForm(data=request.POST)
    if request.method == 'POST' and user_form.is_valid():
        try:
            user = User.objects.create_user(**user_form.cleaned_data)
            registered = True
        except:
            erro = 'existe'
    else:
        user_form = UserForm(data=request.POST)

    return render(request, 'register.html',
                  {'user': user, 'registered': registered, 'erro': erro},)


def ulogin(request):
    '''
        renderiza a paǵina de login
    '''
    erro = None
    if request.method == 'POST':
        name = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(
            username=name,
            password=passw)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'home.html', {})
            else:
                erro = 'errado'
        else:
            erro = 'naoExiste'

    return render(request, 'login.html', {'erro': erro})


@login_required
def ulogout(request):
    '''
        Renderiza a página de logout
    '''
    logout(request)
    return redirect(reverse('nHome'))


@login_required
def home(request):
    '''
        Renderiza a página inical
        Chama a função que valida os períodos de estadias, deixando-os ativou ou não
    '''
    validaEstadia()
    pessoas = Pessoa.objects.all()
    animais = Animal.objects.all()
    estadias = Estadia.objects.filter(ativa=1)
    prioridades = Estadia.objects.filter(ativa=1).order_by('-prioridade')
    resposta = {}
    envio = []
    for prioridade in prioridades:
        resposta = {}
        animal = Animal.objects.get(id=prioridade.animal)
        resposta['animal'] = animal
        resposta['prioridade'] = prioridade
        envio.append(resposta)
    return render(request, 'home.html',
                  {'animais': animais, 'pessoas': pessoas,
                   'estadias': estadias, 'prioridades': envio})


def validaEstadia():
    '''
    Valida as estadias de acordo com a data atual
    '''
    es = Estadia.objects.all()
    hj = datetime.datetime.today()
    for e in es:
        if e.data_saida.month <= hj.month:
            if e.data_saida.day <= hj.day:
                if e.data_saida.year <= hj.year:
                    if e.data_saida.hour > hj.hour:
                        e.ativa = 0
                        e.save()


def naoRolou(request):
    '''
        Página de teste
    '''
    return render(request, 'naoRolou.html', {})


@login_required
def config(request):
    '''
        Renderiza a página de configurações
    '''
    total = Acomodacao.objects.all()
    if total:
        total = total[0].total
    else:
        total = 20
    if request.method == 'POST':
        total = int(request.POST.get('total'))
        pr = int(request.POST.get('prioritarias'))
        p = Quantidade.objects.all()
        if p:
            p.delete()
        prior = Quantidade(qtd=pr)
        prioritarias = pr
        a = Acomodacao.objects.all()
        if a:
            a.delete()
        e = Estadia.objects.filter(ativa=1)
        n = len(e)
        livre = total - n
        b = Acomodacao(total=total, livres=livre)
        b.save()
        return redirect(reverse('nHome'))
    else:
        prioritarias = Quantidade.objects.all()
        if prioritarias:
            prioritarias = prioritarias[0].qtd
        else:
            prioritarias = 5
        return render(request, 'config.html',
                      {'total': total, 'prioridade': prioritarias})
