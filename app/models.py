from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class Pessoas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    pai = models.CharField(max_length=100, verbose_name="Pai da pessoa")
    mae = models.CharField(max_length=100, verbose_name="Mãe da pessoa")
    cpf = models.IntegerField(verbose_name="CPF da pessoa")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.CharField(max_length=100, verbose_name="Email da pessoa")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação da pessoa")

    def __str__(self):
        return f"{self.nome}, {self.cpf}"
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da institução")
    site = models.CharField(max_length=100, verbose_name="Site da instituição")
    telefone = models.CharField(verbose_name="Telefone da instituição")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"


class Area(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área de Saber")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"


class Cursos(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    carga_horaria = models.CharField(verbose_name="Carga horária do curso")
    duracao = models.IntegerField(verbose_name="Duração do curso em meses")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Área de saber do curso")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição do curso")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class Periodo(models.Model):
    periodo = models.IntegerField(verbose_name="Período do curso")
    
    def __str__(self):
        return self.periodo
    
    class Meta:
        verbose_name = "Período"
        verbose_name_plural = "Períodos"


class Disciplinas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Área de saber da disciplina")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


class Matriculas(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição da matrícula")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Curso da matrícula")
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name="Pessoa matriculada")
    data_inicio = models.DateField(verbose_name="Data de início")
    data_previsao_termino = models.DateField(verbose_name="Data de previsão do término")

    def __str__(self):
        return f"{self.pessoa}, {self.curso}"
    
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"


class Avaliacoes(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da avaliação")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Curso da avaliação")
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, verbose_name="Disciplina da avaliação")

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


class Frequencia(models.Model):
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Frequência do curso")
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, verbose_name="Frequência da disciplina")
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name="Frequência da pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de faltas")

    def __str__(self):
        return f"{self.pessoa}, {self.numero_faltas}"
    
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"


class Turmas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da turma")
    periodo = models.CharField(max_length=100, verbose_name="Período da turma")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class Ocorrencias(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da ocorrência")
    data = models.DateField(verbose_name="Data da ocorrência")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Curso da ocorrência")
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, verbose_name="Disciplina da ocorrência")
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name="Pessoa da ocorrência")

    def __str__(self):
        return f"{self.descricao},{self.pessoa}"
    
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"


class DisciplinasporCursos(models.Model):
   
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, verbose_name="Disciplina")
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name="Período")
    carga_horaria = models.CharField(max_length=100, verbose_name="Carga Horária")
    def __str__(self):
        return self.carga_horaria
    
    class Meta:
        verbose_name = "Carga Horária"
        verbose_name_plural = "Cargas Horárias"


class TipodeAvaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do tipo de avaliação")
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"