from django.db import models
from django.conf import settings

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


class Inscricao(models.Model):
    STATUS_CURSO = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Bloqueado'),
        (3, 'Cancelado'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', related_name='inscricao', on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, verbose_name='Curso', related_name='inscricao', on_delete=models.CASCADE)
    status = models.IntegerField(verbose_name='Situacao', choices=STATUS_CURSO, blank=True, default=1)

    data_inscricao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Inscricao')
    atualizado = models.DateTimeField(auto_now=True, verbose_name='Atualizado')

    def __str__(self):
        return self.curso.nome

    def ativar(self):
        self.status = 1
        self.save()


    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        constraints = [
            models.UniqueConstraint(fields=['user', 'curso'], name='unique_curso')
        ]

class AnuncioCurso(models.Model):
    curso = models.ForeignKey(Curso, verbose_name='Curso', on_delete=models.CASCADE)
    titulo = models.CharField(verbose_name='Titulo', max_length=100)
    conteudo = models.TextField('Conteudo')

    data_inscricao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Inscricao')
    atualizado = models.DateTimeField(auto_now=True, verbose_name='Atualizado')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Anuncio_Curso'
        verbose_name_plural='Anuncios_Cursos'
        ordering = ['-data_inscricao']

class Comentarios(models.Model):
    pass
