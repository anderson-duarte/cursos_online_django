from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Inscricao
from .forms import ContatoCurso


def cursos(request):
    cursos = Curso.objects.all()
    contexto = {'cursos':cursos}
    return render(request, 'cursos/cursos.html', contexto)

@login_required
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

@login_required
def inscricao(request, slug):
    curso = get_object_or_404(Curso, slug=slug)

    inscrever, criado = Inscricao.objects.get_or_create(user=request.user, curso=curso)

    if criado:
        messages.success(request, 'Inscrição realizada com sucesso!')
    #     inscrever.ativar()
        return redirect('contas:painel')
    else:
        messages.info(request, 'Você ja está incrito nesse curso.')
        return redirect('contas:painel')

@login_required
def detalhe_curso(request, slug):
    curso = get_object_or_404(Curso, slug=slug)
    return render(request, 'cursos/detalhe_curso.html', {'inscrito': curso})

@login_required
def anuncio_curso(request, slug):
    curso = get_object_or_404(Curso, slug=slug)
    return render(request, 'contas/anuncio_curso.html', {'curso':curso, 'slug': slug})

@login_required
def cancelar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)
    inscricao = get_object_or_404(Inscricao, user=request.user, curso=curso)
    if request.method == 'POST':
        inscricao.delete()
        messages.warning(request, 'Você cancelou a inscrição do curso {}!'.format(curso.nome))
        return redirect('contas:painel')

    return render(request, 'contas/cancelar_curso.html', {'curso':curso, 'inscricao':inscricao})

