from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoa/', PessoasView.as_view(), name='pessoa'),
    path('matricula/', MatriculasView.as_view(), name='matricula'),
    path('instituicao/', InstituicoesView.as_view(), name='instituicao'),
    path('curso/', CursosView.as_view(), name='curso'),
    path('disciplina/', DisciplinasView.as_view(), name='disciplina'),
    path('avaliacao/', AvaliacoesView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciasView.as_view(), name='frequencia'),
    path('turma/', TurmasView.as_view(), name='turma'),
    path('ocorrencia/', OcorrenciasView.as_view(), name='ocorrencia'),
    path('area_saber/', AreaSaberView.as_view(), name='area_saber'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
    path('turno/', TurnoView.as_view(), name='turno'),
]


