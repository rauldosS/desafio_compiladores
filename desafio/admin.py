from django.contrib import admin
from .models import ModelFormArquivo, Caracteres, Linhas

# Register your models here.
@admin.register(ModelFormArquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'versao']

@admin.register(Caracteres)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'arquivo', 'ativo', 'caractere', 'versao']

@admin.register(Linhas)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'arquivo', 'linha', 'versao']