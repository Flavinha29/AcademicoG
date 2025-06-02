from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import (
    Pessoa, Cidade, Ocupacao, InstituicaoEnsino, Curso,
    Disciplina, Matricula, Avaliacao, Frequencia,
    Ocorrencia, Turno
)
from .forms import (
    PessoaForm, CidadeForm, OcupacaoForm, InstituicaoEnsinoForm,
    CursoForm, DisciplinaForm, MatriculaForm, AvaliacaoForm,
    FrequenciaForm, OcorrenciaForm, TurnoForm
)

# Página inicial
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

# Pessoa
class PessoaListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        form = PessoaForm()
        return render(request, 'pessoa_list.html', {'pessoas': pessoas, 'form': form})

    def post(self, request, *args, **kwargs):
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pessoa cadastrada com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar pessoa.")
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa_list.html', {'pessoas': pessoas, 'form': form})

# Cidade
class CidadeListView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        form = CidadeForm()
        return render(request, 'cidades.html', {'cidades': cidades, 'form': form})

    def post(self, request, *args, **kwargs):
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cidade cadastrada com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar cidade.")
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades, 'form': form})

# Ocupação
class OcupacaoListView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        form = OcupacaoForm()
        return render(request, 'ocupações.html', {'ocupacoes': ocupacoes, 'form': form})

    def post(self, request, *args, **kwargs):
        form = OcupacaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ocupação cadastrada com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar ocupação.")
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupações.html', {'ocupacoes': ocupacoes, 'form': form})

# Instituição de Ensino
class InstituicaoEnsinoListView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.all()
        form = InstituicaoEnsinoForm()
        return render(request, 'instituições.html', {'instituicoes': instituicoes, 'form': form})

    def post(self, request, *args, **kwargs):
        form = InstituicaoEnsinoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Instituição cadastrada com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar instituição.")
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituições.html', {'instituicoes': instituicoes, 'form': form})

# Curso
class CursoListView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        form = CursoForm()
        return render(request, 'cursos.html', {'cursos': cursos, 'form': form})

    def post(self, request, *args, **kwargs):
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Curso cadastrado com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar curso.")
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos, 'form': form})

# Disciplina
class DisciplinaListView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        form = DisciplinaForm()
        return render(request, 'curso_disciplinas.html', {'disciplinas': disciplinas, 'form': form})

    def post(self, request, *args, **kwargs):
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Disciplina cadastrada com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar disciplina.")
        disciplinas = Disciplina.objects.all()
        return render(request, 'curso_disciplinas.html', {'disciplinas': disciplinas, 'form': form})

# Matrícula
class MatriculaListView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        form = MatriculaForm()
        return render(request, 'matriculas.html', {'matriculas': matriculas, 'form': form})

    def post(self, request, *args, **kwargs):
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Matrícula cadastrada com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar matrícula.")
        matriculas = Matricula.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas, 'form': form})

# Avaliação
class AvaliacaoListView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        form = AvaliacaoForm()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes, 'form': form})

    def post(self, request, *args, **kwargs):
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Avaliação cadastrada com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar avaliação.")
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes, 'form': form})

# Frequência
class FrequenciaListView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        form = FrequenciaForm()
        return render(request, 'frequencias.html', {'frequencias': frequencias, 'form': form})

    def post(self, request, *args, **kwargs):
        form = FrequenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Frequência cadastrada com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar frequência.")
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencias.html', {'frequencias': frequencias, 'form': form})

# Ocorrência
class OcorrenciaListView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        form = OcorrenciaForm()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias, 'form': form})

    def post(self, request, *args, **kwargs):
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ocorrência cadastrada com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar ocorrência.")
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias, 'form': form})

# Turno
class TurnoListView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turno.objects.all()
        form = TurnoForm()
        return render(request, 'turnos.html', {'turnos': turnos, 'form': form})

    def post(self, request, *args, **kwargs):
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Turno cadastrado com sucesso!")
        else:
            messages.error(request, "Erro ao cadastrar turno.")
        turnos = Turno.objects.all()
        return render(request, 'turnos.html', {'turnos': turnos, 'form': form})
