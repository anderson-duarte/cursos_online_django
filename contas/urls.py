from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'contas'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('cadastre-se/', views.register, name='registrar'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.painel, name='painel'),
    path('editar/', views.editar, name='editar'),
    path('senha/', views.senha, name='senha'),
]