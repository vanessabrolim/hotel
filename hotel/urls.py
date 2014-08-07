from django.conf.urls import patterns, include, url
from django.conf import settings


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'hotel.views.home', name='nHome'),

    # cadastros
    url(r'^cadastro/$', 'hotel.cadastros.Cadastro', name='nCadastro'),
    url(r'^cadastro/animal/(?P<cpf>.*)/?$',
        'hotel.cadastros.CadastroAnimal', name='nCadastroAnimal'),
    url(r'^cadastro/pessoaInicial/$', 'hotel.cadastros.CadastroPessoaInicial',
        name='nCadastroPessoaInicial'),
    url(r'^cadastro/animalInicial/$', 'hotel.cadastros.CadastroAnimalInicial',
        name='nCadastroAnimalInicial'),
    url(r'^cadastro/animalSecundario/(?P<cpf>.*)/?$',
        'hotel.cadastros.CadastroAnimalSecundario',
        name='nCadastroAnimalSecundario'),
    url(r'^cadastro/pessoa/(?P<cpf>.*)/?$',
        'hotel.cadastros.CadastroPessoa', name='nCadastroPessoa'),
    url(r'^cadastro/cumprimento/$', 'hotel.cadastros.CadastroCumprimento',
        name='nCadastroCumprimento'),
    url(r'^cadastro/estadiaInicial$', 'hotel.cadastros.CadastroEstadiaInicial',
        name='nCadastroEstadiaInicial'),
    url(r'^cadastro/estadiaSecundario/(?P<cpf>.*)/$', 
        'hotel.cadastros.CadastroEstadiaSecundario',
        name='nCadastroEstadiaSecundario'),
    url(r'^cadastro/estadia/(?P<id>.*)$', 'hotel.cadastros.CadastroEstadia',
        name='nCadastroEstadia'),
    url(r'^cadastro/recomendacaoInicial$', 'hotel.cadastros.CadastroRecomendacaoInicial',
        name='nCadastroRecomendacaoInicial'),
    url(r'^cadastro/recomendacaoSecundaria/(?P<cpf>.*)/$', 'hotel.cadastros.CadastroRecomendacaoSecundaria',
        name='nCadastroRecomendacaoSecundaria'),
    url(r'^cadastro/recomendacaoTerceira/(?P<id>.*)/$', 'hotel.cadastros.CadastroRecomendacaoTerceira',
        name='nCadastroRecomendacaoTerceira'),
    url(r'^cadastro/recomendacao/(?P<id>.*)/$', 'hotel.cadastros.CadastroRecomendacao',
        name='nCadastroRecomendacao'),

    # relatorios
    url(r'^relatorios/$', 'hotel.views.Relatorios', name='nRelatorios'),
    url(r'^relatorios/recomendacoes/hoje/$',
        'hotel.views.RecDia', name='nRecomendacoesHoje'),
    url(r'^relatorios/recomendacoes/ontem/$',
        'hotel.views.RecAmanha', name='nRecomendacoesAmanha'),
    url(r'^relatorios/recomendacoes/amanha/$', 'hotel.views.RecOntem',
        name='nRecomendacoesOntem'),
    url(r'^relatorios/hospedados/$', 'hotel.views.Hospedados',
        name='nHospedados'),
    url(r'^relatorios/livres/$', 'hotel.views.Livres',
        name='nLivres'),
    url(r'^relatorios/estadia/animal/$', 'hotel.views.EstadiaAnimal',
        name='nEstadiaAnimal'),
    url(r'^relatorios/estadia/pessoa/$', 'hotel.views.EstadiaPessoa',
        name='nEstadiaPessoa'),

    # edicoes
    url(r'^editar/$', 'hotel.edicoes.Editar', name='nEdicao'),
    url(r'^editar/pessoa/inicial/$', 'hotel.edicoes.EditarPessoaInicial',
        name='nEditarPessoaInicial'),
    url(r'^editar/animal/inicial/$', 'hotel.edicoes.EditarAnimalInicial',
        name='nEditarAnimalInicial'),
    url(r'^editar/animal/secundario/(?P<cpf>.*)/?/$',
        'hotel.edicoes.EditarAnimalSecundario', name='nEditarAnimalSecundario'),
    url(r'^editar/animal/(?P<id>\d+)/$',
        'hotel.edicoes.EditarAnimal', name='nEditaAnimal'),
    url(r'^editar/pessoa/(?P<cpf>.*)/?/$',
        'hotel.edicoes.EditarPessoa', name='nEditaPessoa'),
    url(r'^editar/recomendacao/(?P<id>\d+)/$',
        'hotel.edicoes.EditarRecomendacao', name='nEditaRecomendacao'),

    # outros e testes
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^naoRolou/$', 'hotel.views.naoRolou', name='nnaoRolou')
)
