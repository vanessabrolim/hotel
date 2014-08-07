#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from models import *
from forms import *
import datetime
from django.utils.dateformat import DateFormat


def Cadastro(request):
    return render(request, 'cadastros/cadastro.html', {})


def CadastroPessoaInicial(request):
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


def CadastroPessoa(request, cpf):
    form = FormPessoa(request.POST)
    if request.method == "POST" and form.is_valid():
        form.save()
        cpf = request.POST.get('cpf')
        pessoa = Pessoa.objects.get(cpf=cpf)
        return render(request,
                      'cadastros/sucessoPessoa.html', {'pessoa': pessoa, })
    else:
        form = FormPessoa()
    return render(request, 'cadastros/cadastroPessoa.html', {'cpf': cpf, })


def CadastroAnimalInicial(request):
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


def CadastroAnimalSecundario(request, cpf):
    if Animal.objects.filter(dono=cpf):
        animais = Animal.objects.filter(dono=cpf)
        return render(request, 'cadastros/cadastroAnimalSecundario.html',
                      {'animais': animais, 'cpf': cpf, })
    else:
        return redirect(reverse('nCadastroAnimal', kwargs={'cpf': cpf}))


def CadastroAnimal(request, cpf):
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


def CadastroEstadiaInicial(request):
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


def CadastroEstadiaSecundario(request, cpf):
    if Animal.objects.filter(dono=cpf):
        animais = Animal.objects.filter(dono=cpf)
        return render(request, 'cadastros/cadastroEstadiaSecundario.html',
                      {'animais': animais, 'cpf': cpf, })
    else:
        return redirect(reverse('nCadastroAnimal', kwargs={'cpf': cpf}))


def CadastroEstadia(request, id):
    form = FormEstadia(request.POST)
    agora = datetime.datetime.today()
    ano = str(agora.year)
    mes = agora.month
    dia = agora.day
    if mes < 10:
        mes = '0'+str(mes)
    if dia < 10:
        dia = '0'+str(dia)
    hoje = dia+'/'+mes+'/'+ano
    if request.method == 'POST':
        form.data_entrada = datetime.datetime.strptime(
            request.POST.get('data_entrada'), "%d/%m/%Y")
        form.data_saida = datetime.datetime.strptime(
            request.POST.get('data_saida'), "%d/%m/%Y")
        form.horario_entrada = datetime.datetime.strptime(
            request.POST.get('horario_entrada'), "%H:%M")
        form.horario_saida = datetime.datetime.strptime(
            request.POST.get('horario_saida'), "%H:%M")
    if request.method == "POST" and form.is_valid():
        estadia = form.save()
        if request.POST.get('data_entrada') == hoje:
            estadia.ativa = 1
            estadia.save()
        animal = Animal.objects.get(id=estadia.animal)
        dono = Pessoa.objects.get(cpf=animal.dono)
        return render(request, 'cadastros/sucessoEstadia.html',
                      {'estadia': estadia, 'animal': animal.nome,
                       'dono': dono.nome})
    else:
        form = FormEstadia()
    id=1
    return render(request, 'cadastros/cadastroEstadia.html',
                  {'form': form, 'animal': id})


def CadastroRecomendacaoInicial(request):
    form = FormCPF(request.POST)
    cpf = request.POST.get('cpf')
    if request.method == "POST" and form.is_valid():
        if Pessoa.objects.filter(cpf=cpf):
            return redirect(reverse('nCadastroRecomendacaoSecundaria',
                                    kwargs={'cpf': cpf}))
        else:
            return redirect(reverse('nCadastroPessoa', kwargs={'cpf': cpf}))
    else:
        form = FormCPF()

    return render(request, 'cadastros/cadastroRecomendacaoInicial.html',
                  {'form': form})


def CadastroRecomendacaoSecundaria(request, cpf):
    if Animal.objects.filter(dono=cpf):
        animais = Animal.objects.filter(dono=cpf)
        estadias = []
        for animal in animais:
            estadiasT = Estadia.objects.filter(animal=animal.id)
            for estadis in estadiasT:
                if estadis.ativa:
                    estadis.nomeAnimal = animal.nome
                    estadias.append(estadis)
        return render(request, 'cadastros/cadastroRecomendacaoSecundaria.html',
                      {'estadias': estadias, 'cpf': cpf, })
    else:
        return redirect(reverse('nCadastroAnimal', kwargs={'cpf': cpf}))


def CadastroRecomendacaoTerceira(request, id):
    if Estadia.objects.filter(animal=id):
        estadias = Estadia.objects.filter(animal=id)
        return render(request, 'cadastros/cadastroRecomendacao.html',
                      {'estadias': estadias, 'id': id, })
    else:
        return redirect(reverse('nCadastroEstadia', kwargs={'id': id}))


def CadastroRecomendacao(request,id):
    form = FormRecomendacao(request.POST)
    if request.method == "POST" and form.is_valid():
        recomendacao = form.save()
        return HttpResponseRedirect(reverse('nHome'))
    else:
        form = FormRecomendacao()

    return render(request, 'cadastros/cadastroRecomendacao.html',
                  {'form': form, })


def CadastroCumprimento(request):
    form = FormCumprimento(request.POST)
    if request.method == "POST" and form.is_valid():
        cumprimento = form.save()
        return HttpResponseRedirect(reverse('nHome'))
    else:
        form = FormCumprimento()

    return render(request, 'cadastros/CadastroCumprimento.html',
                  {'form': form, })
