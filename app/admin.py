

from django.contrib import admin
from .models import *


class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInline]


class CursoInstituicaoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoInstituicaoInline]


class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]


class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]


class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'uf']

admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Pessoa)
admin.site.register(InstituicaoEnsino, InstituicaoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
# admin.site.register(Turno)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(AvaliacaoTipo)

