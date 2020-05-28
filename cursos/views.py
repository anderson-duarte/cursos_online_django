from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Inscricao, AnuncioCurso, Licao, Material
from .forms import ContatoCurso, ComentariosForm
from .decorators import incricao_requerida


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
@incricao_requerida
def detalhe_curso(request, slug):
    curso = request.curso
    return render(request, 'cursos/detalhe_curso.html', {'inscrito': curso})

@login_required
@incricao_requerida
def anuncio_curso(request, slug):
    curso = request.curso
    return render(request, 'cursos/anuncio_curso.html', {'curso':curso, 'anuncios': curso.usuario_anuncios.all()})

@login_required
def cancelar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)
    inscricao = get_object_or_404(Inscricao, user=request.user, curso=curso)
    if request.method == 'POST':
        inscricao.delete()
        messages.warning(request, 'Você cancelou a inscrição do curso {}!'.format(curso.nome))
        return redirect('contas:painel')

    return render(request, 'contas/cancelar_curso.html', {'curso':curso, 'inscricao':inscricao})

@login_required
@incricao_requerida
def comentarios(request, slug, pk):
    curso1 = request.curso
    comentario = get_object_or_404(curso1.usuario_anuncios.all(), pk=pk)
    form = ComentariosForm(request.POST or None)
    if form.is_valid():
        coment = form.save(commit=False)
        coment.user = request.user
        coment.anuncio_curso = get_object_or_404(AnuncioCurso, curso=curso1)
        coment.save()
        form = ComentariosForm()
        messages.success(request, 'Comentário enviado com sucesso')
    contexto = {'curso':curso1, 'comentario':comentario, 'form': form}
    return render(request, 'cursos/mostrar_aula.html', contexto)

@login_required
@incricao_requerida
def licoes(request, slug):
    curso = request.curso
    return render(request, 'cursos/licoes.html', {'curso':curso})

@login_required
@incricao_requerida
def licoes(request, slug):
    curso=request.curso
    licoes = curso.licoes_disponiveis()
    if request.user.is_staff:
        licoes = curso.licoes.all()
    contexto = {
        'curso': curso,
        'licoes': licoes
    }
    return render(request, 'cursos/licoes.html', contexto)

@login_required
@incricao_requerida
def licao(request, slug, pk):
    curso=request.curso
    licao = get_object_or_404(Licao, pk=pk, curso=curso)
    material = Material.objects.filter(licao=licao)

    if not request.user.is_staff and not licao.esta_disponivel():
        messages.error(request, 'Aula Indisponivel')
        return redirect('cursos:licoes', slug=curso.slug)

    contexto = {'curso': curso, 'licao': licao, 'material':material}
    return render(request, 'cursos/licao.html', contexto)

@login_required
@incricao_requerida
def material(request, slug, pk):
    curso = request.curso
    material = get_object_or_404(Material, pk=pk, licao__curso=curso)
    licao = material.licao

    if not request.user.is_staff and not licao.esta_disponivel():
        messages.error(request, 'Material Indisponivel')
        return redirect('cursos:licao', slug=curso.slug, pk=licao.pk)
    if not material.is_midia():
        return redirect(material.arquivo.url)
    contexto ={'curso' : curso, 'licao':licao, 'material':material}
    return render(request, 'cursos/arquivo.html', contexto)