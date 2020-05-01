from django.shortcuts import render
from .models import Curso
from .forms import ContatoCurso
from django.http import HttpResponse
# Create your views here.

def cursos(request):
    cursos = Curso.objects.all()
    contexto = {'cursos':cursos}
    return render(request, 'cursos/cursos.html', contexto)

def curso(request, slug):
    cursinho = Curso.objects.get(slug=slug)
    contexto = {}
    if request.method == 'POST':
        form = ContatoCurso(request.POST)
        if form.is_valid():
            form.send_mail(cursinho)
            envio = True
            contexto['envio'] = envio
            form = ContatoCurso()
    else:
        form = ContatoCurso()
    contexto['form'] = form
    contexto['curso'] = cursinho
    return render(request, 'cursos/curso.html', contexto)
