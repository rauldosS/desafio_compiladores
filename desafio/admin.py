from django.contrib import admin
from .models import ModelFormArquivo, Caracteres

# Register your models here.
@admin.register(ModelFormArquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo']

@admin.register(Caracteres)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'arquivo', 'ativo', 'caractere']