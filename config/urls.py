from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
path('admin/', admin.site.urls),
path('', TemplateView.as_view(template_name='index.html'), name='index'),
path('pessoas/', PessoasView.as_view(), name='pessoas'),
path('cursos/', CursosView.as_view(), name='cursos'),
path('area/', AreaView.as_view(), name='area'),
path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
path('instituicao/', InstituicaoView.as_view(), name='instituicao'),
path('periodo/', PeriodoView.as_view(), name='periodo'),
path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
path('matriculas/', MatriculasView.as_view(), name='matriculas'),
path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacoes'),
path('frequencia/', FrequenciaView.as_view(), name='frequencia'),
path('turmas/', TurmasView.as_view(), name='turmas'),
path('cidade/', CidadeView.as_view(), name='cidade'),
path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencias'),
path('disciplinasporcursos/', DisciplinasporCursosView.as_view(), name='disciplinasporcursos'),
path('tipodeavaliacao/', TipodeAvaliacaoView.as_view(), name='tipodeavaliacao'),

]