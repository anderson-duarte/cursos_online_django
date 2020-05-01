from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeForm
from .forms import RegisterForm, EditarUsuario
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('core:index')
    else:
        form = RegisterForm()
    contexto = {'form': form}
    return render(request, 'contas/registrar.html', contexto)

@login_required
def painel(request):
    return render(request, 'contas/admin_cursos.html')

def editar(request):
    sucess = False
    if request.method == 'POST':
      form = EditarUsuario(request.POST, instance=request.user)
      if form.is_valid():
          form.save()
          form = EditarUsuario(instance=request.user)
          sucess = True
    else:
        form = EditarUsuario(instance=request.user)
    context = {'form': form, 'sucess':sucess}
    return render(request, 'contas/edit.html', context)

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
