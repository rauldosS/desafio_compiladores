from django.contrib import admin
from .models import ModelFormArquivo, Caracteres, Linhas, Palavras, Numeros, Simbolos, Atributos, AssociacaoSimboloAtributo

# Register your models here.
@admin.register(ModelFormArquivo)
class ArquivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'versao']

@admin.register(Caracteres)
class CaractereAdmin(admin.ModelAdmin):
    list_display = ['id', 'arquivo', 'sequencia', 'ativo', 'asci', 'caractere', 'versao']
    list_filter = ['ativo', 'versao']

@admin.register(Palavras)
class PalavraAdmin(admin.ModelAdmin):
    list_display = ['id', 'arquivo', 'sequencia', 'palavra', 'versao']
    list_filter = ['arquivo', 'versao']
    search_fields = ['palavra']

@admin.register(Linhas)
class LinhasAdmin(admin.ModelAdmin):
    list_display = ['id', 'arquivo', 'linha', 'versao']

@admin.register(Numeros)
class Número(admin.ModelAdmin):
    list_display = ['id', 'inteiro', 'decimal']

@admin.register(Simbolos)
class SimboloAdmin(admin.ModelAdmin):
    list_display = ['id', 'simbolo']
    search_fields  = ['simbolo']

@admin.register(Atributos)
class AtributoAdmin(admin.ModelAdmin):
    list_display = ['id', 'atributo']

@admin.register(AssociacaoSimboloAtributo)
class AssociacaoSimboloAtributoAdmin(admin.ModelAdmin):
    list_display = ['id', 'simbolo', 'atributo']
