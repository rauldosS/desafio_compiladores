from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import EnvioArquivo
from . import views

app_name = 'desafio'

urlpatterns = [
   path('', views.inicio, name='inicio'),
   path('inicio/', views.inicio, name='inicio'),
   path('enviar_arquivo/', EnvioArquivo.as_view(), name='enviar_arquivo'),
   path('arquivo/<int:id>/', views.arquivo, name='arquivo'),
   path('arquivos_enviados/', views.arquivos_enviados, name='arquivos_enviados'),
   path('decompor_arquivo/<int:id>/', views.decompor_arquivo, name='decompor_arquivo'),
   path('atualizar_arquivo_completo/', views.atualizar_arquivo_completo, name='atualizar_arquivo_completo')
]