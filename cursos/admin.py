from django.contrib import admin

# Register your models here.
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'inicio']
    search_fields = ['nome']
    prepopulated_fields = {'slug':('nome',)}


admin.site.register(Curso, CursoAdmin)