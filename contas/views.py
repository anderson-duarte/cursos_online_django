from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeForm
from .forms import CriarAluno, EditarAluno
# Create your views here.
from django.views.generic import CreateView
#Resolveu o erro abaixo
#Attempted relative import beyond toplevel package django project on make migrations
from cursos.models import Curso, Inscricao
from django.http import HttpResponse


@login_required
def painel(request):
    cursus = Inscricao.objects.filter(user=request.user)
    return render(request, 'contas/admin_cursos.html', {'cursos':cursus})

@login_required
def senha(request):
    sucess = False
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            sucess = True
            update_session_auth_hash(request, form.user)
#            return redirect('/account/profile')
    else:
        form = PasswordChangeForm(request.user)
    contexto = {'form':form, 'sucess': sucess}
    return render(request, 'contas/senha.html', contexto)

class cadastrar(CreateView):
    form_class = CriarAluno
    success_url = ('/accounts/login/')
    context_object_name = 'form'
    template_name = 'contas/novo.html'

@login_required
def editar(request):
    sucess = False
    if request.method == 'POST':
        form = EditarAluno(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditarAluno(instance=request.user)
            sucess = True
    else:
        form = EditarAluno(instance=request.user)
    contexto = {'form': form, 'sucess': sucess}
    return render(request, 'contas/edit.html', contexto)
