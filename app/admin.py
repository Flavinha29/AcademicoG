# app/admin.py

from django.contrib import admin
from .models import *

# Inline para RF04 e RF05
class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

# Inline para RF03 e RF05
class CursoInstituicaoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoInstituicaoInline]

# Inline para RF02 e RF01
class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

# Inline para RF14
class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]

# Inline para RF09
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

# Inline para RF12
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'uf']

# Registro padrão
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
admin.site.register(Turno)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(AvaliacaoTipo)
