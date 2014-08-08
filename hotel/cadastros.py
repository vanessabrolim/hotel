#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from models import *
from forms import *
import datetime
from django.utils.dateformat import DateFormat


@login_required
def Cadastro(request):
    ''' Renderiza a página de cadastro'''
    return render(request, 'cadastros/cadastro.html', {})


@login_required
def CadastroPessoaInicial(request):
    ''' 
        Usando o CPF do input, busca por pessoas com esse CPF. Se já existirem,
        redireciona para a edição do cadastro. Senão, envia para cadastrar.
    '''
    form = FormCPF(request.POST)
    cpf = request.POST.get('cpf')
    nome = request.POST.get('nome')
    if request.method == "POST" and form.is_valid():
        if Pessoa.objects.filter(cpf=cpf):
            return redirect(reverse('nEditaPessoa', kwargs={'cpf': cpf}))
        else:
            return redirect(reverse('nCadastroPessoa', kwargs={'cpf': cpf}))
    else:
        form = FormCPF()

    return render(request, 'cadastros/cadastroPessoaInicial.html',
                  {'cpf': cpf, })


@login_required
def CadastroPessoa(request, cpf):
    '''
        Faz novo cadastro e redireciona para página de sucesso
    '''
    form = FormPessoa(request.POST)
    if request.method == 'POST':
        form.cpf = int(request.POST.get('cpf'))
    if request.method == "POST" and form.is_valid():
        form.save()
        cpf = request.POST.get('cpf')
        pessoa = Pessoa.objects.get(cpf=cpf)
        return render(request,
                      'cadastros/sucessoPessoa.html', {'pessoa': pessoa, })
    else:
        form = FormPessoa()
    return render(request, 'cadastros/cadastroPessoa.html', {'cpf': cpf, })


@login_required
def CadastroAnimalInicial(request):
    '''
        Busca por pessoa, a partir do cpf, para listar os animais que estão ligados à pessoa
    '''
    form = FormCPF(request.POST)
    cpf = request.POST.get('cpf')
    if request.method == "POST" and form.is_valid():
        if Pessoa.objects.filter(cpf=cpf):
            return redirect(reverse('nCadastroAnimalSecundario',
                                    kwargs={'cpf': cpf}))
        else:
            return redirect(reverse('nCadastroPessoa', kwargs={'cpf': cpf}))
    else:
        form = FormCPF()

    return render(request, 'cadastros/cadastroAnimalInicial.html',
                  {'cpf': cpf, })


@login_required
def CadastroAnimalSecundario(request, cpf):
    '''
        Retorna todos os animais que a pessoa possui, caso não possua nenhum envia para cadastro de animais
    '''
    if Animal.objects.filter(dono=cpf):
        animais = Animal.objects.filter(dono=cpf)
        return render(request, 'cadastros/cadastroAnimalSecundario.html',
                      {'animais': animais, 'cpf': cpf, })
    else:
        return redirect(reverse('nCadastroAnimal', kwargs={'cpf': cpf}))


@login_required
def CadastroAnimal(request, cpf):
    '''
        Faz novo cadastro de animal e redireciona para página de sucesso
    '''
    if request.method == "POST":
        form = FormAnimal(request.POST)
        if form.is_valid():
            animal = form.save()
            animal.save()
        return render(request, 'cadastros/sucessoAnimal.html',
                      {'animal': animal, })

    else:
        form = FormAnimal()

    return render(request, 'cadastros/cadastroAnimal.html',
                  {'form': form, 'cpf': cpf, })


@login_required
def CadastroEstadiaInicial(request):
    '''
        Pede o CPF para buscar a pessoas e os animais que pertencem a ela.
        Se a pessoa não existir, redireciona para novo cadastro
    '''
    form = FormCPF(request.POST)
    cpf = request.POST.get('cpf')
    if request.method == "POST" and form.is_valid():
        if Pessoa.objects.filter(cpf=cpf):
            return redirect(reverse('nCadastroEstadiaSecundario',
                                    kwargs={'cpf': cpf}))
        else:
            return redirect(reverse('nCadastroPessoa', kwargs={'cpf': cpf}))
    else:
        form = FormCPF()

    return render(request, 'cadastros/cadastroAnimalInicial.html',
                  {'cpf': cpf, })


@login_required
def CadastroEstadiaSecundario(request, cpf):
    '''
        Lista os animais que pertencem à pessoa
    '''
    if Animal.objects.filter(dono=cpf):
        animais = Animal.objects.filter(dono=cpf)
        return render(request, 'cadastros/cadastroEstadiaSecundario.html',
                      {'animais': animais, 'cpf': cpf, })
    else:
        return redirect(reverse('nCadastroAnimal', kwargs={'cpf': cpf}))


@login_required
def CadastroEstadia(request, id):
    '''
        Faz novo cadastro de estadia
        Se a estadia for na data atual, deixa-a ativa
        Subtrai uma acomocação
    '''
    form = FormEstadia(request.POST)
    agora = datetime.datetime.today()
    ano = str(agora.year)
    mes = agora.month
    dia = agora.day
    if mes < 10:
        mes = '0' + str(mes)
    if dia < 10:
        dia = '0' + str(dia)
    hoje = dia + '/' + mes + '/' + ano
    if request.method == 'POST':
        prioridade = int(request.POST.get('prioridade'))
        de = request.POST.get(
            'data_entrada') + ' ' + request.POST.get('horario_entrada')
        form.data_entrada = datetime.datetime.strptime(de, "%d/%m/%Y %H:%M")
        ds = request.POST.get(
            'data_saida') + ' ' + request.POST.get('horario_saida')
        form.data_saida = datetime.datetime.strptime(ds, "%d/%m/%Y %H:%M")
    if request.method == "POST" and form.is_valid():
        estadia = form.save()
        if request.POST.get('data_entrada') <= hoje:
            estadia.ativa = 1
            estadia.save()
        a = Acomodacao.objects.all()
        qtd = a[0].livres
        nova = Acomodacao(total=a[0].total, livres=qtd - 1)
        a.delete()
        nova.save()
        animal = Animal.objects.get(id=estadia.animal)
        dono = Pessoa.objects.get(cpf=animal.dono)
        return render(request, 'cadastros/sucessoEstadia.html',
                      {'form': form, 'animal': animal.nome,
                       'dono': dono.nome, 'estadia': estadia})
    else:
        form = FormEstadia()
    return render(request, 'cadastros/cadastroEstadia.html',
                  {'form': form, 'animal': id})
