from django import forms
from .models import (
    Pessoa, Cidade, Ocupacao, InstituicaoEnsino, Curso,
    Disciplina, Matricula, Avaliacao, Frequencia, Ocorrencia, Turno
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',
            'pai',
            'mae',
            'cpf',
            'data_nasc',
            'email',
            'cidade',
            'ocupacao',
            Submit('submit', 'Salvar')
        )

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CidadeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',
            'uf',
            Submit('submit', 'Salvar')
        )

class OcupacaoForm(forms.ModelForm):
    class Meta:
        model = Ocupacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OcupacaoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',  # Corrigi de 'descricao' para 'nome' conforme seu model
            Submit('submit', 'Salvar')
        )

class InstituicaoEnsinoForm(forms.ModelForm):
    class Meta:
        model = InstituicaoEnsino
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InstituicaoEnsinoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',
            'site',   # Corrigido para 'site' que é o campo no seu model
            'telefone', # Corrigido para 'telefone' que é o campo no seu model
            'cidade',
            Submit('submit', 'Salvar')
        )

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',
            'carga_horaria_total',  # corrigido para os campos do model
            'duracao_meses',
            'area',
            'instituicao',
            Submit('submit', 'Salvar')
        )

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DisciplinaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',
            'area',
            Submit('submit', 'Salvar')
        )

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MatriculaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'instituicao',
            'curso',
            'pessoa',
            'data_inicio',
            'data_previsao_termino',
            Submit('submit', 'Salvar')
        )

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AvaliacaoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'descricao',
            'curso',
            'disciplina',
            'tipo',
            Submit('submit', 'Salvar')
        )

class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FrequenciaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'curso',
            'disciplina',
            'pessoa',
            'numero_faltas',
            Submit('submit', 'Salvar')
        )

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OcorrenciaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'descricao',
            'data',
            'curso',
            'disciplina',
            'pessoa',
            Submit('submit', 'Salvar')
        )

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['nome']

    def __init__(self, *args, **kwargs):
        super(TurnoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',
            Submit('submit', 'Salvar')
        )
