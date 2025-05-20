# app/views.py

from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class PessoasView(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoas.html', {'pessoas': pessoas})

class CursosView(View):
    def get(self, request):
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})

class DisciplinasView(View):
    def get(self, request):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})
