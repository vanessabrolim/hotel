from django import forms
from models import *


class FormAnimal (forms.ModelForm):

    class Meta(object):
        model = animal


class FormPessoa (forms.ModelForm):

    class Meta(object):
        model = pessoa


class FormCumprimento (forms.ModelForm):

    class Meta(object):
        model = cumprimento


class FormRecomendacao (forms.ModelForm):

    class Meta(object):
        model = recomendacao


class FormEstadia (forms.ModelForm):

    class Meta(object):
        model = estadia
