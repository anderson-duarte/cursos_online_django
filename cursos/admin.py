from django.contrib import admin

# Register your models here.
from .models import Curso, Inscricao, AnuncioCurso, Comentarios

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'inicio']
    search_fields = ['nome']
    prepopulated_fields = {'slug':('nome',)}

class IncricaoAdmin(admin.ModelAdmin):
    list_display = ['user', 'curso', 'status']

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['anuncio_curso', 'data_inscricao', 'user']

admin.site.register(Curso, CursoAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(Inscricao, IncricaoAdmin)
admin.site.register([AnuncioCurso])