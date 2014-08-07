from django import forms
from models import *


class FormAnimal (forms.ModelForm):

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


class FormCumprimento (forms.ModelForm):

    class Meta(object):
        model = Cumprimento


class FormRecomendacao (forms.ModelForm):

    class Meta(object):
        model = Recomendacao


class FormEstadia (forms.ModelForm):
    data_entrada= forms.DateField(
        widget=forms.widgets.DateInput(format="%d/%m/%Y"))
    data_saida= forms.DateField(
        widget=forms.widgets.DateInput(format="%d/%m/%Y"))

    class Meta(object):
        model = Estadia
