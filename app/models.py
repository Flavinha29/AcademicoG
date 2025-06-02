from django.db import models

# RF12 - Cidades
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


# RF02 - Ocupações
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


# RF01 - Pessoas
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    nome_do_pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    nome_da_mae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(max_length=100, verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


# RF03 - Instituições de Ensino
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição")
    site = models.CharField(max_length=100, verbose_name="Site")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"


# RF04 - Áreas do Saber
class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da área")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"


# RF05 - Cursos
class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga horária total")
    duracao_meses = models.IntegerField(verbose_name="Duração (meses)")
    area = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


# RF06 - Turnos
class Turno(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"


# RF07 - Disciplinas
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


# RF08 - Matrículas
class Matricula(models.Model):
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField(verbose_name="Data de início")
    data_previsao_termino = models.DateField(verbose_name="Data prevista de término")

    def __str__(self):
        return f'{self.pessoa} - {self.curso}'

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"


# RF15 - Tipos de Avaliação
class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do tipo de avaliação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"


# RF09 - Avaliações
class Avaliacao(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    nota = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Nota")
    avaliacao_tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Tipo de avaliação")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


# RF10 - Frequência
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de faltas")

    def __str__(self):
        return f'{self.pessoa} - {self.disciplina}'

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"


# RF11 - Turmas
class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da turma")
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name="Turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


# RF13 - Ocorrências
class Ocorrencia(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"


# RF14 - Disciplinas por Curso com Turno
class CursoDisciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name="Turno")
    carga_horaria = models.IntegerField(verbose_name="Carga horária")
    periodo = models.CharField(max_length=20, verbose_name="Período")

    def __str__(self):
        return f'{self.disciplina} - {self.curso}'

    class Meta:
        verbose_name = "Disciplina por Curso"
        verbose_name_plural = "Disciplinas por Curso"
