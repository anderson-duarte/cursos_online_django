from django.urls import path

from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.cursos, name='cursos'),
    path('<str:slug>/', views.curso, name='curso'),
    path('inscricao/<str:slug>/', views.inscricao, name='inscrever'),
]