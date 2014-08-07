from django.db import models


class Pessoa (models.Model):
    nome = models.CharField(max_length=50)
    telefoneCel = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)


class Animal (models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    idade = models.IntegerField()
    pelagem = models.CharField(max_length=50)
    caracteristica_marcante = models.CharField(max_length=50)
    dono = models.IntegerField()


class Cumprimento (models.Model):
    horario = models.TimeField()


class Recomendacao (models.Model):
    MEDICAMENTOSA = 'med'
    ALIMENTAR = 'al'
    SOCIAL = 'soc'
    OUTRA = 'outra'
    TIPO_ESCOLHAS = (
        (MEDICAMENTOSA, 'Medicamentosa'),
        (ALIMENTAR, 'Alimentar'),
        (SOCIAL, 'Social'),
        (OUTRA, 'Outra')
    )
    estadia = models.IntegerField()
    tipo = models.CharField(
        max_length=50, choices=TIPO_ESCOLHAS, default=OUTRA)
    intervalo_horario = models.IntegerField()
    ultimo_horario = models.TimeField()
    recomendacao = models.CharField(max_length=50)
    #cumprida = models.ManyToManyField(Cumprimento)


class Estadia (models.Model):
    animal = models.IntegerField()
    data_entrada = models.DateField()
    horario_entrada = models.TimeField()
    data_saida = models.DateField()
    horario_saida = models.TimeField()
    forma = models.CharField(max_length=15)
    observacao = models.CharField(max_length=80)
    ativa = models.IntegerField()
