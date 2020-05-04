from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Aluno


# class EditeUserForm(forms.ModelForm):
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
#         if queryset.exists():
#             raise forms.ValidationError('Este email ja foi cadastrado!')
#         else:
#             return email
#
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#
# class EditarAluno(forms.ModelForm):
#
#     class Meta:
#         model = Aluno
#         fields = ['nome', 'sexo', 'cpf', 'escolaridade', 'profissao']
#
# class AlunoForm(forms.ModelForm):
#     class Meta:
#         model = Aluno
#         fields = ['nome', 'sexo', 'cpf', 'escolaridade', 'profissao']
#
# class UserForm(forms.ModelForm):
#     password = forms.CharField(max_length=32, widget=forms.PasswordInput)
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
#         if queryset.exists():
#             raise forms.ValidationError('Este email ja foi cadastrado!')
#         else:
#             return email
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email']

class CriarAluno(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = Aluno.objects.filter(email=email)
        if queryset.exists():
            raise forms.ValidationError('Este email ja foi cadastrado!')
        else:
            return email
    class Meta(UserCreationForm):
        model = Aluno
        fields = ('nome', 'email', 'sexo', 'cpf', 'escolaridade', 'profissao', 'username')

class EditarAluno(UserChangeForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = Aluno.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Este email ja foi cadastrado!')
        else:
            return email
    class Meta(UserChangeForm):
        model = Aluno
        fields = ('nome', 'email', 'sexo', 'cpf', 'escolaridade', 'profissao', 'username')






