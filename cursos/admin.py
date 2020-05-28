from django.contrib import admin

# Register your models here.
from .models import Curso, Inscricao, AnuncioCurso, Comentarios,Material, Licao

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'inicio']
    search_fields = ['nome']
    prepopulated_fields = {'slug':('nome',)}

class IncricaoAdmin(admin.ModelAdmin):
    list_display = ['user', 'curso', 'status']

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['anuncio_curso', 'data_inscricao', 'user']

class MaterialInline(admin.TabularInline):
    model = Material

class LicaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'numero', 'curso', 'data_disponibilizacao']
    search_fields = ['nome', 'curso', 'data_disponibilizacao']
    list_filter = ['data_licao']
    inlines = [MaterialInline]

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['nome', 'licao']

admin.site.register(Curso, CursoAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(Inscricao, IncricaoAdmin)
admin.site.register([AnuncioCurso])
admin.site.register(Licao, LicaoAdmin)
admin.site.register(Material, MaterialAdmin)
