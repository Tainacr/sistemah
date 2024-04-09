from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoas.objects.all()
        return render(request, 'pessoas.html', {'pessoas': pessoas})

class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacao': ocupacao})

class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicao = Instituicao.objects.all()
        return render(request, 'instituicao.html', {'instituicao': instituicao})
    
class AreaView(View):
    def get(self, request, *args, **kwargs):
        area = Area.objects.all()
        return render(request, 'area.html', {'area': area})

class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Cursos.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})

class PeriodoView(View):
    def get(self, request, *args, **kwargs):
        periodo = Periodo.objects.all()
        return render(request, 'periodo.html', {'periodo': periodo})

class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplinas.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})
    
class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matriculas.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas})
    
class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacoes.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencia = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencia': frequencia})

class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turmas.objects.all()
        return render(request, 'turmas.html', {'turmas': turmas})

class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidade = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidade': cidade})

class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencias.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})

class DisciplinasporCursosView(View):
    def get(self, request, *args, **kwargs):
        disciplinasporcursos = DisciplinasporCursos.objects.all()
        return render(request, 'disciplinasporcursos.html', {'disciplinasporcursos': disciplinasporcursos})

class TipodeAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipodeavaliacao = TipodeAvaliacao.objects.all()
        return render(request, 'tipodeavaliacao.html', {'tipodeavaliacao': tipodeavaliacao})
