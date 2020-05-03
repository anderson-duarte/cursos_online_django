from django.contrib import admin
from .models import Aluno
from .forms import CriarAluno, EditarAluno
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AlunoAdmin(UserAdmin):
    add_form = CriarAluno
    form = EditarAluno
    model = Aluno
    list_display = ['username', 'nome', 'escolaridade', 'profissao']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nome', 'escolaridade', 'profissao')}),
    )

admin.site.register(Aluno, AlunoAdmin)


