from django.contrib import admin
from .models import (
    Cidade, Ocupacao, Pessoa, InstituicaoEnsino, Curso, Turno,
    Disciplina, Matricula, Avaliacao, Frequencia, Turma,
    Ocorrencia, CursoDisciplina, AvaliacaoTipo, AreaSaber
)

# Inline para Matricula dentro de Pessoa
class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1
    fk_name = 'pessoa'  # Especifica o campo FK em Matricula para Pessoa

# Inline para Frequencia dentro de Pessoa
class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1
    fk_name = 'pessoa'  # Especifica o campo FK em Frequencia para Pessoa

class PessoaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline, FrequenciaInline]
    list_display = ('nome', 'cpf', 'email', 'cidade', 'ocupacao')
    search_fields = ('nome', 'cpf', 'email')

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline, AvaliacaoInline]

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

class TurmaAdmin(admin.ModelAdmin):
    pass

class MatriculaAdmin(admin.ModelAdmin):
    pass

# Registro dos modelos no admin
admin.site.register(Cidade)
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Pessoa, PessoaAdmin)  # <-- Aqui, usando PessoaAdmin com inlines
admin.site.register(InstituicaoEnsino)
admin.site.register(AreaSaber)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turno)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Matricula, MatriculaAdmin)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(AvaliacaoTipo)
