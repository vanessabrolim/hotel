from django.conf.urls import patterns, include, url
from django.conf import settings


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^home/$', 'hotel.views.home', name='nHome'),
    # cadastros
    url(r'^cadastro/animal/$', 'hotel.views.CadastroAnimal', name='nCadastroAnimal'),
    url(r'^cadastro/pessoa/$', 'hotel.views.CadastroPessoa', name='nCadastroPessoa'),
    url(r'^cadastro/cumprimento/$', 'hotel.views.CadastroCumprimento',
        name='nCadastroCumprimento'),
    url(r'^cadastro/estadia/$', 'hotel.views.CadastroEstadia',
        name='nCadastroEstadia'),
    url(r'^cadastro/recomendacao/$', 'hotel.views.CadastroRecomendacao',
        name='nCadastroRecomendacao'),

    # pesquisas
    url(r'^pesquisa/animal/$', 'hotel.views.PesquisaAnimal', name='nPesquisaAnimal'),
    url(r'^pesquisa/pessoa/$', 'hotel.views.PesquisaPessoa', name='nPesquisaPessoa'),
    url(r'^pesquisa/estadia/$', 'hotel.views.PesquisaEstadia',
        name='nPesquisaEstadia'),

    # edicoes
    url(r'^editar/animal/(?P<id>\d+)/$',
        'hotel.views.EditaAnimal', name='nEditaAnimal'),
    url(r'^editar/pessoa/(?P<id>\d+)/$',
        'hotel.views.EditaPessoa', name='nEditaPessoa'),
    url(r'^editar/recomendacao/(?P<id>\d+)/$',
        'hotel.views.EditaRecomendacao', name='nEditaRecomendacao'),

    # outros e testes
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
