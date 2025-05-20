# config/urls.py

from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
]
