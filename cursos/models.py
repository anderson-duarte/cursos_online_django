from django.db import models

# Create your models here.



class CursoManager(models.Manager):
    def busca(self, query):
        return self.get_queryset().filter(models.Q(nome__icontains=query) | models.Q(descricao__icontains=query))


class Curso(models.Model):

    nome = models.CharField(max_length=150, verbose_name='Nome')
    slug = models.SlugField(verbose_name='Atalho')
    descricao = models.TextField(verbose_name='Descricao', blank=True)
    sobre = models.TextField(verbose_name='Descricao reduzida', blank=True)
    inicio = models.DateField(verbose_name='Data de Inicio', null=True, blank=True)
    imagem = models.ImageField(upload_to='imagens/', verbose_name='Inserir Imagem', null=True, blank=True)
    criado = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    modificado = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    def __str__(self):
        return self.nome

    def mostrar_imagem(self):
        if self.imagem =='':
            return False
        else:
            return True

    objects = CursoManager()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural='Cursos'