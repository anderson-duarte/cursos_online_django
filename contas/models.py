from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

SEXO = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]

class Aluno(AbstractUser):
    nome = models.CharField(verbose_name='Nome', max_length=100)
    sexo = models.CharField(verbose_name='Sexo', max_length=20, choices=SEXO)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    escolaridade = models.CharField(verbose_name='Escolaridade', max_length=50)
    profissao = models.CharField(verbose_name='Profissão', max_length=70)
    cadastrado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True, verbose_name='ALterado')

    def __str__(self):
        return self.nome


class ResetSenha(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', on_delete=models.CASCADE, related_name='resets')
    key = models.CharField(verbose_name='Chave', max_length=100, unique=True)
    criado = models.DateTimeField(auto_now_add=True, verbose_name='Criado em', )
    confirmado = models.BooleanField(default=False, blank=True, verbose_name='Confirmado?')

    def __str__(self):
        return self.user + ' em '+ self.criado

    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-criado']