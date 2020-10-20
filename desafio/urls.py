from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import EnvioArquivo
from . import views

app_name = 'desafio'

urlpatterns = [
   path('', views.inicio, name='desafio'),
   path('enviado/', views.inicio, name='enviado'),
   path('arquivo/<int:id>/', views.arquivo, name='arquivo'),
   path('arquivos_enviados/', views.arquivos_enviados, name='arquivos_enviados'),
   path('enviar_arquivo/', EnvioArquivo.as_view(), name='enviar_arquivo'),
   path('decompor_arquivo/<int:id>/', views.decompor_arquivo, name='decompor_arquivo')
]