from django.template import RequestContext
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from models import *
from forms import *


def home(request):
    global context
    context = RequestContext(request)
    pessoas = Pessoa.objects.all()
    animais = Animal.objects.all()
    return render(request, 'home.html', {'animais':animais, 'pessoas':pessoas})


def CadastroAnimal(request):
    form = FormAnimal(request.POST)
    if request.method == "POST" and form.is_valid():
        animal = form.save()
        return HttpResponseRedirect(reverse('nHome'))
    else:
        form = FormAnimal()

    return render(request, 'CadastroAnimal.html', {'form': form, })


def CadastroPessoa(request):
    form = FormPessoa(request.POST)
    if request.method == "POST" and form.is_valid():
        p = form.save()
        return HttpResponseRedirect(reverse('nHome'))
    else:
        form = FormPessoa()

    return render(request, 'cadastroPessoa.html', {'form': form, })


def CadastroCumprimento(request):
    form = FormCumprimento(request.POST)
    if request.method == "POST" and form.is_valid():
        cumprimento = form.save()
        return HttpResponseRedirect(reverse('nHome'))
    else:
        form = FormCumprimento()

    return render(request, 'CadastroCumprimento.html', {'form': form, })


def CadastroRecomendacao(request):
    form = FormRecomendacao(request.POST)
    if request.method == "POST" and form.is_valid():
        recomendacao = form.save()
        return HttpResponseRedirect(reverse('nHome'))
    else:
        form = FormRecomendacao()

    return render(request, 'CadastroRecomendacao.html', {'form': form, })


def CadastroEstadia(request):
    form = FormEstadia(request.POST)
    if request.method == "POST" and form.is_valid():
        estadiaa = form.save()
        return HttpResponseRedirect(reverse('nHome'))
    else:
        form = FormEstadia()

    return render(request, 'CadastroEstadia.html', {'form': form, })


def PesquisaAnimal(request):
    return True


def PesquisaPessoa(request):
    return True


def PesquisaEstadia(request):
    return True


def EditaAnimal(request):
    return True


def EditaPessoa(request):
    return True


def EditaRecomendacao(request):
    return True
