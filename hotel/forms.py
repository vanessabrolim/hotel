from django import forms
from models import *


class FormAnimal (forms.ModelForm):

    class Meta(object):
        model = Animal


class FormPessoa (forms.ModelForm):

    class Meta(object):
        model = Pessoa


class FormCumprimento (forms.ModelForm):

    class Meta(object):
        model = Cumprimento


class FormRecomendacao (forms.ModelForm):

    class Meta(object):
        model = Recomendacao


class FormEstadia (forms.ModelForm):

    class Meta(object):
        model = Estadia
