from django.urls import path
from . import views

app_name = 'contas'

urlpatterns = [
    path('', views.painel, name='painel'),
    path('editar/', views.editar, name='editar'),
    path('senha/', views.senha, name='senha'),
    path('cadastre-se/', views.cadastrar.as_view(), name='novo'),
]