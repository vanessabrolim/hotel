from django import forms
from django.contrib.auth.models import User
from models import *


class UserForm(forms.ModelForm):

    class Meta(object):
        model = User
        fields = ('username', 'password')


class FormAnimal (forms.ModelForm):
    caracteristica_marcante = forms.CharField(required=False)

    class Meta(object):
        model = Animal


class FormPessoa (forms.ModelForm):
    telefone = forms.CharField(required=False)

    class Meta(object):
        model = Pessoa


class FormCPF (forms.ModelForm):

    class Meta(object):
        model = Pessoa
        fields = ('cpf',)


class FormEstadia (forms.ModelForm):
    observacao = forms.CharField(required=False)

    class Meta(object):
        model = Estadia
