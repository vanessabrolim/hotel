#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from models import *
from forms import *


@login_required
def Relatorios(request):
    '''
        Renderiza a página com os links de relatórios
    '''
    return render(request, 'relatorios/relatorios.html', {})


@login_required
def RecDia(request):
    '''
        Renderiza os relatórios com as recomendações para o dia
    '''
    return render(request, 'relatorios/recomendacoesHoje.html', {})


@login_required
def Hospedados(request):
    '''
        Renderiza o relatório com os animais hospedados
    '''
    estadias = Estadia.objects.filter(ativa=1)
    resposta = {}
    envio = []
    for estadia in estadias:
        resposta = {}
        animal = Animal.objects.get(id=estadia.animal)
        pessoa = Pessoa.objects.get(cpf=animal.dono)
        resposta['animal'] = animal
        resposta['pessoa'] = pessoa
        resposta['estadia'] = estadia
        envio.append(resposta)

    return render(request, 'relatorios/hospedados.html',
                  {'envio': envio, })


@login_required
def Livres(request):
    '''
        Renderiza o relatorio com as acomodações livres
    '''
    a = Acomodacao.objects.all()
    acomodacao = a[0]
    return render(request, 'relatorios/livres.html',
                  {'acomodacao': acomodacao})


@login_required
def AnimalInicial(request):
    '''
        Renderiza página com pedido de parte do nome do animal
    '''
    if request.method == 'POST':
        a = Animal.objects.filter(nome__icontains=request.POST.get('nome'))
        return render(request, 'relatorios/estadiaAnimal.html', {'animais': a})
    else:
        return render(request, 'relatorios/animalInicial.html', {})


@login_required
def EstadiaAnimal(request):
    '''
        Lista os animais que no nome a string digitada
    '''
    return render(request, 'relatorios/estadiaAnimal.html', {})


@login_required
def DetalheAnimal(request, id):
    '''
        Renderiza a página com todos os detalhes de um animal
    '''
    a = Animal.objects.get(id=id)
    dono = Pessoa.objects.get(cpf=a.dono)
    estadia = Estadia.objects.get(animal=id, ativa=1)
    rec = Recomendacao.objects.filter(estadia=estadia.id)
    return render(request, 'relatorios/detalheAnimal.html',
                  {'animal': a, 'dono': dono, 'estadia': estadia,
                   'recomendacoes': rec})


@login_required
def PessoaInicial(request):
    '''
        Renderiza a página com  a lista de pessoas que tem a string de entrada
        no nome
    '''
    if request.method == 'POST':
        a = Pessoa.objects.filter(nome__icontains=request.POST.get('nome'))
        return render(request, 'relatorios/estadiaPessoa.html', {'pessoas': a})
    else:
        return render(request, 'relatorios/pessoaInicial.html', {})


@login_required
def DetalhePessoa(request, id):
    '''
        Renderiza a página com os detalhes da pessoa e de seus animais
    '''
    p = Pessoa.objects.get(id=id)
    a = Animal.objects.filter(dono=p.cpf)
    return render(request, 'relatorios/detalhePessoa.html',
                  {'animais': a, 'pessoa': p, })
