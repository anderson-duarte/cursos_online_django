from django.db import models
from django.contrib.auth.models import AbstractUser

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

