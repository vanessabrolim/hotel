from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from models import *
from forms import *
import datetime


@login_required
def Editar(request):
    '''
        Renderiza a pagina com os links para edição
    '''
    return render(request, 'alteracoes/edita.html', {})


@login_required
def EditarAnimalInicial(request):
    '''
        Pede o CPF para buscar os animais ligadoas à pessoa
    '''
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


@login_required
def EditarAnimalSecundario(request, cpf):
    if Animal.objects.filter(dono=cpf):
        animais = Animal.objects.filter(dono=cpf)
        return render(request, 'alteracoes/editaAnimalSecundario.html',
                      {'animais': animais, 'cpf': cpf, })
    else:
        return redirect(reverse('nCadastroAnimal', kwargs={'cpf': cpf}))


@login_required
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


@login_required
def EditarPessoaInicial(request):
    '''
        Lista os animais ligados à pessoa e verifica se existe alguma estadia ligada à pessoa
    '''
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


@login_required
def EditarPessoa(request, cpf):
    '''
        Edita o cadastro de uma pessoa
    '''
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


@login_required
def EditaEstadiaInicial(request):
    '''
        Busca por pessoas com o CPF, caso não existe redireciona para cadastro
    '''
    form = FormCPF(request.POST)
    cpf = request.POST.get('cpf')
    if request.method == "POST" and form.is_valid():
        if Pessoa.objects.filter(cpf=cpf):
            return redirect(reverse('nEditaEstadiaSecundario',
                                    kwargs={'cpf': cpf}))
        else:
            return redirect(reverse('nCadastroPessoa', kwargs={'cpf': cpf}))
    else:
        form = FormCPF()

    return render(request, 'alteracoes/editaEstadiaInicial.html',
                  {'cpf': cpf, })


@login_required
def EditaEstadiaSecundario(request, cpf):
    '''
        Lista os animais ligados à pessoa
    '''
    if Animal.objects.filter(dono=cpf):
        animais = Animal.objects.filter(dono=cpf)
        return render(request, 'alteracoes/editaEstadiaSecundario.html',
                      {'animais': animais, 'cpf': cpf, })
    else:
        return redirect(reverse('nCadastroAnimal', kwargs={'cpf': cpf}))


@login_required
def EditaEstadia(request, id):
    '''
        Edita estadia, ativa a estadia caso o período de estadia
        inclua a data atual
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
        e = Estadia.objects.filter(animal=id)
        e.delete()
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
        animal = Animal.objects.get(id=estadia.animal)
        dono = Pessoa.objects.get(cpf=animal.dono)
        return render(request, 'alteracoes/sucessoEstadia.html',
                      {'form': form, 'animal': animal.nome,
                       'dono': dono.nome, 'estadia': estadia})
    else:
        form = FormEstadia()
    estadia = Estadia.objects.get(animal=id)
    return render(request, 'alteracoes/editaEstadia.html',
                  {'form': form, 'animal': id, 'estadia': estadia})
