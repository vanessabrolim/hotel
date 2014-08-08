from django.db import models


class Pessoa (models.Model):
    nome = models.CharField(max_length=50)
    telefoneCel = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    cpf = models.IntegerField()


class Animal (models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    idade = models.IntegerField()
    pelagem = models.CharField(max_length=50)
    caracteristica_marcante = models.CharField(max_length=50)
    dono = models.IntegerField()


class Acomodacao(models.Model):
    total = models.IntegerField(default=20)
    livres = models.IntegerField(default=20)

class Quantidade(models.Model):
    qtd = models.IntegerField(default=5)


class Estadia (models.Model):
    animal = models.IntegerField()
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField()
    forma = models.CharField(max_length=15)
    observacao = models.CharField(max_length=80)
    ativa = models.IntegerField()
    recomendacao = models.CharField(max_length=150)
    prioridade = models.IntegerField()
