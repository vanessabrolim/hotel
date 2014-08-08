from django.conf.urls import patterns, include, url
from django.conf import settings


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'hotel.views.home', name='nHome'),
    url(r'^configuracoes/$', 'hotel.views.config', name='nConfig'),
    url(r'^login/$', 'hotel.views.ulogin', name='nLogin'),
    url(r'^logout/$', 'hotel.views.ulogout', name='nLogout'),
    url(r'^register/$', 'hotel.views.register', name='nRegister'),

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
    #url(r'^cadastro/cumprimento/$', 'hotel.cadastros.CadastroCumprimento',
    #    name='nCadastroCumprimento'),
    url(r'^cadastro/estadiaInicial$', 'hotel.cadastros.CadastroEstadiaInicial',
        name='nCadastroEstadiaInicial'),
    url(r'^cadastro/estadiaSecundario/(?P<cpf>.*)/$', 
        'hotel.cadastros.CadastroEstadiaSecundario',
        name='nCadastroEstadiaSecundario'),
    url(r'^cadastro/estadia/(?P<id>.*)$', 'hotel.cadastros.CadastroEstadia',
        name='nCadastroEstadia'),
    # url(r'^cadastro/recomendacaoInicial$', 'hotel.cadastros.CadastroRecomendacaoInicial',
    #     name='nCadastroRecomendacaoInicial'),
    # url(r'^cadastro/recomendacaoSecundaria/(?P<cpf>.*)/$', 'hotel.cadastros.CadastroRecomendacaoSecundaria',
    #     name='nCadastroRecomendacaoSecundaria'),
    # url(r'^cadastro/recomendacaoTerceira/(?P<id>.*)/$', 'hotel.cadastros.CadastroRecomendacaoTerceira',
    #     name='nCadastroRecomendacaoTerceira'),
    # url(r'^cadastro/recomendacao/(?P<id>.*)/$', 'hotel.cadastros.CadastroRecomendacao',
    #     name='nCadastroRecomendacao'),

    # relatorios
    url(r'^relatorios/$', 'hotel.relatorios.Relatorios', name='nRelatorios'),
    # url(r'^relatorios/recomendacoesHoje/$',
    #     'hotel.relatorios.RecDia', name='nRecomendacoesHoje'),
    # url(r'^relatorios/recomendacoesOntem/$',
    #     'hotel.relatorios.RecAmanha', name='nRecomendacoesAmanha'),
    # url(r'^relatorios/recomendacoesAmanha/$', 'hotel.relatorios.RecOntem',
    #     name='nRecomendacoesOntem'),
    url(r'^relatorios/hospedados/$', 'hotel.relatorios.Hospedados',
        name='nHospedados'),
    url(r'^relatorios/livres/$', 'hotel.relatorios.Livres',
        name='nLivres'),
    url(r'^relatorios/animalInicial/$', 'hotel.relatorios.AnimalInicial',
        name='nAnimalInicial'),
    url(r'^relatorios/estadiaAnimal/$', 'hotel.relatorios.EstadiaAnimal',
        name='nEstadiaAnimal'),
    url(r'^relatorios/detalheAnimal/(?P<id>.*)$', 'hotel.relatorios.DetalheAnimal',
        name='nDetalheAnimal'),
    url(r'^relatorios/pessoaInicial/$', 'hotel.relatorios.PessoaInicial',
        name='nPessoaInicial'),
    url(r'^relatorios/detalhePessoa/(?P<id>.*)$', 'hotel.relatorios.DetalhePessoa',
        name='nDetalhePessoa'),

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
    #url(r'^editar/recomendacao/inicial/$',
    #   'hotel.edicoes.EditarRecomendacaoInicial', name='nEditaRecomendacaoInicial'),
     url(r'^editar/estadia/inicial/$', 'hotel.edicoes.EditaEstadiaInicial',
        name='nEditarEstadiaInicial'),
     url(r'^editar/estadia/secundario/(?P<cpf>.*)/?/$', 'hotel.edicoes.EditaEstadiaSecundario',
        name='nEditaEstadiaSecundario'),
     url(r'^editar/estadia/(?P<id>.*)/?/$', 'hotel.edicoes.EditaEstadia',
        name='nEditaEstadia'),


    # outros e testes
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^naoRolou/$', 'hotel.views.naoRolou', name='nnaoRolou')
)
