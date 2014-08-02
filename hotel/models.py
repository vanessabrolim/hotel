from django.db import models


class animal (models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    idade = models.IntegerField()
    pelagem = models.CharField(max_length=50)
    caracteristica_marcante = models.CharField(max_length=50)


class pessoa (models.Model):
    nome = models.CharField(max_length=50)
    telefoneCel = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    animais = models.ManyToManyField(animal)


class cumprimento (models.Model):
    horario = models.TimeField()


class recomendacao (models.Model):
    animal = models.ForeignKey('animal')
    tipo = models.CharField(max_length=50)
    intervalo_horario = models.IntegerField()
    ultimo_horario = models.TimeField()
    cumprida = models.ManyToManyField(cumprimento)


class estadia (models.Model):
    animal = models.ForeignKey('animal')
    dataEntrada = models.DateField()
    horario_entrada = models.TimeField()
    data_saida = models.DateField()
    horario_saida = models.TimeField()
    forma = models.CharField(max_length=15)
    observacao = models.CharField(max_length=80)
    recomendacoes = models.ManyToManyField(recomendacao)
