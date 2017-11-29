from django.shortcuts import render, redirect
from cadastros.models import *
from cadastros.forms import AlunoForm, MatriculaForm
from questionario.forms import QuestaoForm
from questionario.models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from cadastros.models import Aluno, DisciplinaOfertada, Disciplina, Matricula, Turma

# Create your views here.
def home(request):
    return render(request, "index.html")

def cursos(request):
    return render(request, "cursos.html")

def boletim(request):
    return render(request, "boletim.html")

def noticias(request):
    return render(request, "noticias.html")

def grade(request):
    return render(request, "grade-curricular.html")

def detalhes(request):
    return render(request, "detalhes.html")

def checa_aluno(usuario):
    return usuario.perfil == "A"

def checa_professor(usuario):
    return usuario.perfil == "P"

def corrige_gabarito(gabarito, resposta):
    i = 0
    nota = 0
    while i < 10:
        if resposta[i] == gabarito[i]:
            nota += 1
        i+=1 
    return nota

@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def pagina_aluno(request):
    aluno = Aluno.objects.get(id=request.user.id)
    disciplinas = DisciplinaOfertada.objects.all()
    disciplinas_matriculadas = Matricula.objects.filter(ra_aluno=aluno)
    questoes = Questao.objects.all()
    arquivos_questoes = ArquivoQuestao.objects.all()
    respostas = Resposta.objects.all()
    lista_respostas = []
    for resposta in respostas:
        lista_respostas.append(resposta.numero_questao)
    lista_disciplinas = []
    lista_turmas = []
    for disciplina in disciplinas_matriculadas:
        lista_disciplinas.append(disciplina.nome_disciplina.nome_disciplina)
        lista_turmas.append(disciplina.id_turma)
    
    context = {
        'curso' : aluno.sigla_curso.nome,
        'disciplinasOfertadas' : disciplinas,
        'disciplinas_matriculadas' : disciplinas_matriculadas,
        'lista_disciplinas' : lista_disciplinas,
        'lista_turmas' : lista_turmas,
        'arquivos_questoes' : arquivos_questoes,
        'questoes' : questoes
    }

    return render(request, "pagina_aluno.html", context)

@login_required(login_url="/login")
@user_passes_test(checa_professor)
def pagina_professor(request):
    turmas = Turma.objects.filter(ra_professor=request.user.ra)
    respostas = Resposta.objects.all()
    context = {
        'turmas' : turmas,
        'respostas' : respostas
    }

    return render(request, "pagina_professor.html", context)

def contato(request):
    return render(request, "contato.html")

def matricula(request):
    if request.POST:
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AlunoForm()
        

    context = {
        'form' : form
    }
    #django-widget-tweaks

    return render(request, "matricula.html", context)

def matricula_disciplina(request):
    if request.POST:
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MatriculaForm()

    context = {
        'form' : form
    }

    return render(request, "matricula_disciplina.html", context)

'''
@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def tec_web(request):
    if request.POST:
        form = MatriculaForm(request.POST)
        form.ra_aluno = request.user.ra
        if form.is_valid():
            forms = form.save(commit=False)
            forms.ra_aluno = Aluno.objects.get(id=request.user.id)
            forms.nome_disciplina = DisciplinaOfertada.objects.get(nome_disciplina=1)
            forms.ano_ofertado = DisciplinaOfertada.objects.get(nome_disciplina=1)
            forms.semestre_ofertado = DisciplinaOfertada.objects.get(nome_disciplina=1)
            forms.save()
    else:
        form = MatriculaForm()

    disciplina = Disciplina.objects.get(nome="Tecnologia Web")
    context = {
        'disciplina' : disciplina,
        'form' : form,
        'user' : request.user
    }

    return render(request, "tec-web.html", context)
'''

def disciplina(request, slug):
    disciplina = Disciplina.objects.get(slug=slug)
    aluno = Aluno.objects.get(id=request.user.id)
    matriculas = Matricula.objects.filter(ra_aluno=aluno)
    lista_matriculas = []
    for item in matriculas:
        lista_matriculas.append(item.nome_disciplina.nome_disciplina.nome)
    if request.POST:
        form = MatriculaForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.ra_aluno = Aluno.objects.get(id=request.user.id)
            forms.nome_disciplina = DisciplinaOfertada.objects.get(nome_disciplina=disciplina)
            forms.ano_ofertado = DisciplinaOfertada.objects.get(nome_disciplina=disciplina)
            forms.semestre_ofertado = DisciplinaOfertada.objects.get(nome_disciplina=disciplina)
            forms.save()
    else:
        form = MatriculaForm()

    context = {
        'matriculas' : lista_matriculas,
        'disciplina' : disciplina,
        'form' : form,
        'user' : request.user
    }

    return render(request, "disciplina.html", context)
