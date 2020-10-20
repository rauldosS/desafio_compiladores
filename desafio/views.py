from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .models import ModelFormArquivo, Caracteres, Linhas
from .forms import FormularioArquivo
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

# Create your views here.
class EnvioArquivo(CreateView):
    model = ModelFormArquivo
    form_class = FormularioArquivo
    template_name = 'desafio/enviar_arquivo.html'

    success_url = reverse_lazy('desafio:enviado')

def inicio(request):
    arquivos = ModelFormArquivo.objects.all()

    return render(request, 'desafio/index.html', {'arquivos': arquivos})

def envio_arquivo(request):
    if request.method == 'POST':
        form = ModelFormArquivo(request.POST, request.FILES)
        if form.is_valid():
            # salvar arquivo
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormArquivo()
    return render(request, 'envio.html', {'form': form})

def arquivo(request, id=1):
    arquivo = ModelFormArquivo.objects.get(id=id)
    caracteres = Caracteres.objects.filter(arquivo=arquivo, versao=arquivo.versao).order_by('sequencia')
    linhas = Linhas.objects.filter(arquivo=arquivo, versao=arquivo.versao).order_by('linha')

    dados = {
        'arquivo': arquivo,
        'caracteres': caracteres,
        'linhas': linhas
    }

    return render(request, 'desafio/arquivo/arquivo.html', dados)

def decompor_arquivo(request, id=1):
    arquivo = ModelFormArquivo.objects.get(id=id)
    caminho_arquivo = arquivo.arquivo

    versao = arquivo.versao + 1

    atualizar_arquivo(id, versao)
    decompor_caracteres(arquivo, versao)
    atualizar_linhas(arquivo, versao)

    return redirect('desafio:arquivo', id=arquivo.id)

def atualizar_arquivo(id, versao):
    try:
        registro = ModelFormArquivo.objects.get(id=id)
        conteudo = open(str(registro.arquivo), 'r').read()

        registro.conteudo = conteudo,
        registro.versao = versao

        registro.save()
    except:
        print('Erro ao atualizar arquivo')

def decompor_caracteres(arquivo, versao):
    conteudo = open(str(arquivo.arquivo), 'r').read()
    sequencia = 1
    for palavra in str.split(conteudo):
        ascII = ''.join(str(ord(c)) for c in palavra)
        registro = Caracteres.objects.create(
            arquivo = arquivo, 
            caractere = ascII,
            sequencia = sequencia,
            palavra = palavra,
            versao = versao, 
        )   
        sequencia += 1 

        try:
            registro.save()
        except registro:
            pass

def atualizar_linhas(arquivo, versao):
    linhas_arquivo = arquivo.arquivo.readlines()
    contagem_linha = 1
    for linha in linhas_arquivo:
        print(f'Linha {contagem_linha}: {linha.strip()}')

        registro = Linhas.objects.create(
            arquivo=arquivo,
            conteudo=linha.strip(),
            linha=contagem_linha,
            versao=versao
        )

        contagem_linha += 1

        try:
            registro.save()
        except registro:
            pass

def arquivos_enviados(request):
    arquivos = ModelFormArquivo.objects.all()

    return render(request, 'desafio/arquivos_enviados.html', {'arquivos': arquivos})