from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from models import *
from forms import *
import datetime


def Editar(request):
    return render(request, 'alteracoes/edita.html', {})


def EditarAnimalInicial(request):
    form = FormCPF(request.POST)
    cpf = request.POST.get('cpf')
    if request.method == "POST" and form.is_valid():
        if Pessoa.objects.filter(cpf=cpf):
            return redirect(reverse('nEditarAnimalSecundario',
                                    kwargs={'cpf': cpf}))
        else:
            return redirect(reverse('nCadastroPessoa', kwargs={'cpf': cpf}))
    else:
        form = FormCPF()

    return render(request, 'alteracoes/editaAnimalInicial.html',
                  {'cpf': cpf, })


def EditarAnimalSecundario(request, cpf):
    if Animal.objects.filter(dono=cpf):
        animais = Animal.objects.filter(dono=cpf)
        return render(request, 'alteracoes/editaAnimalSecundario.html',
                      {'animais': animais, 'cpf': cpf, })
    else:
        return redirect(reverse('nCadastroAnimal', kwargs={'cpf': cpf}))


def EditarAnimal(request, id):
    animais = Animal.objects.filter(id=id)
    animal = animais[0]
    form = FormAnimal(request.POST)
    if request.method == 'POST' and form.is_valid():
        animal.delete()
        a = form.save()
        return render(request, 'alteracoes/sucessoAnimal.html',
                      {'animal': a})
    return render(request, 'alteracoes/EditaAnimal.html',
                  {'animal': animal})


def EditarPessoaInicial(request):
    form = FormCPF(request.POST)
    cpf = request.POST.get('cpf')
    if request.method == "POST" and form.is_valid():
        if Pessoa.objects.filter(cpf=cpf):
            return redirect(reverse('nEditaPessoa', kwargs={'cpf': cpf}))
        else:
            return redirect(reverse('nCadastroPessoa', kwargs={'cpf': cpf}))
    else:
        form = FormCPF()

    return render(request, 'alteracoes/editaPessoaInicial.html',
                  {'cpf': cpf, })


def EditarPessoa(request, cpf):
    pessoas = Pessoa.objects.filter(cpf=cpf)
    p = pessoas[0]
    form = FormPessoa(request.POST)
    if request.method == 'POST' and form.is_valid():
        p.delete()
        form.save()
        cpf = request.POST.get('cpf')
        pessoa = Pessoa.objects.get(cpf=cpf)
        #pessoa = alterado[0]
        return render(request, 'alteracoes/sucessoPessoa.html',
                      {'pessoa': pessoa})
    return render(request, 'alteracoes/alteraPessoa.html', {'pessoa': p})


def EditarRecomendacao(request):
    return True
