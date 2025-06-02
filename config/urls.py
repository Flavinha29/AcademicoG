from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView,
    PessoaListView,
    CidadeListView,
    OcupacaoListView,
    InstituicaoEnsinoListView,
    CursoListView,
    DisciplinaListView,
    MatriculaListView,
    AvaliacaoListView,
    FrequenciaListView,
    OcorrenciaListView,
    TurnoListView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('pessoas/', PessoaListView.as_view(), name='pessoa_list'),
    
    path('cidades/', CidadeListView.as_view(), name='cidade_list'),

    path('ocupacoes/', OcupacaoListView.as_view(), name='ocupacao_list'),

    path('instituicoes/', InstituicaoEnsinoListView.as_view(), name='instituicao_list'),

    path('cursos/', CursoListView.as_view(), name='curso_list'),

    path('disciplinas/', DisciplinaListView.as_view(), name='disciplina_list'),

    path('matriculas/', MatriculaListView.as_view(), name='matricula_list'),

    path('avaliacoes/', AvaliacaoListView.as_view(), name='avaliacao_list'),

    path('frequencia/', FrequenciaListView.as_view(), name='frequencia_list'),

    path('ocorrencias/', OcorrenciaListView.as_view(), name='ocorrencia_list'),

    path('turnos/', TurnoListView.as_view(), name='turno_list'),
]
