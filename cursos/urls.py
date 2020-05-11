from django.urls import path

from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.cursos, name='cursos'),
    path('<str:slug>/', views.curso, name='curso'),
    path('inscricao/<str:slug>/', views.inscricao, name='inscrever'),
    path('detalhe/<str:slug>/', views.detalhe_curso, name='detalhe'),
    path('anuncio_curso/<str:slug>/', views.anuncio_curso, name='anuncio'),
    path('cancelar_curso/<int:id_curso>/', views.cancelar_curso, name='deletar_curso'),
]