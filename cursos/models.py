from django.db import models
from django.conf import settings
from core.mail import send_mail_temmplate
from django.shortcuts import render, get_object_or_404

# Create your models here.
from django.utils import timezone


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

    def licoes_disponiveis(self):
        hoje = timezone.now().date()
        return self.licoes.filter(data_disponibilizacao__gte=hoje)


    objects = CursoManager()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural='Cursos'


class Licao(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100)
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    numero = models.IntegerField(verbose_name='Numero da aula', blank=True, default=0)
    data_disponibilizacao = models.DateField(verbose_name='Data disponibilização', blank=True, null=True)

    curso = models.ForeignKey(Curso, verbose_name='Curso', on_delete=models.CASCADE, related_name='licoes')
    data_licao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado = models.DateTimeField(auto_now=True, verbose_name='Atualizado')

    def __str__(self):
        return self.nome

    def esta_disponivel(self):
        if self.data_disponibilizacao:
            hoje = timezone.now().date()
            return self.data_disponibilizacao >= hoje
        return False

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural='Aulas'
        ordering = ['numero']

class Material(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100)
    midia = models.TextField(verbose_name='Midia', blank=True)
    arquivo = models.FileField(verbose_name='Arquivo', blank=True, upload_to='material/licao', null=True)

    licao = models.ForeignKey(Licao, verbose_name='Licao', on_delete=models.CASCADE, related_name='materiais')

    def is_midia(self):
        return bool(self.midia)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural='Materiais'


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

    def aprovado(self):
        return self.status == 1

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        constraints = [
            models.UniqueConstraint(fields=['user', 'curso'], name='unique_curso')
        ]

class AnuncioCurso(models.Model):
    curso = models.ForeignKey(Curso, verbose_name='Curso', on_delete=models.CASCADE, related_name='usuario_anuncios')
    titulo = models.CharField(verbose_name='Titulo', max_length=100)
    conteudo = models.TextField('Conteudo')

    data_inscricao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado = models.DateTimeField(auto_now=True, verbose_name='Atualizado')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Anuncio_Curso'
        verbose_name_plural='Anuncios_Cursos'
        ordering = ['-data_inscricao']
        db_table = 'comentarios_curso'

class Comentarios(models.Model):
    anuncio_curso = models.ForeignKey(AnuncioCurso, verbose_name="Anuncio", related_name='comentarios', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', on_delete=models.CASCADE)
    comentario = models.TextField(verbose_name='Comentario')

    data_inscricao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado = models.DateTimeField(auto_now=True, verbose_name='Atualizado')

    def __str__(self):
        return str(self.anuncio_curso)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural='Comentarios'
        ordering = ['-data_inscricao']





# def post_save_inscricao(instance, created, ** kwargs):
#     if created:
#             subject = instance.curso
#             context= {
#                 'inscricao': instance
#             }
#             inscrito  = Inscricao.objects.filter(curso=instance.curso)[:1]
#             recipient_list=[inscrito.user.email]
#             send_mail_temmplate(subject, 'cursos/inscricao_mail.html', context, recipient_list)
#
#
# models.signals.post_save.connect(
#     post_save_inscricao, sender=Inscricao, dispatch_uid='post_save_inscricao'
# )
