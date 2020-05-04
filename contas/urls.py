from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'contas'

urlpatterns = [

    path('', views.painel, name='painel'),
    path('editar/', views.editar, name='editar'),
    path('senha/', views.senha, name='senha'),
    path('cadastre-se/', views.cadastrar.as_view(), name='novo'),
]