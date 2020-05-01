from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='index'),
    path('contato/', views.contato, name='contato'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)