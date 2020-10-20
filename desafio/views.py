from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import ModelFormArquivo, Caracteres
from .forms import FormularioArquivo
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

# Create your views here.
def inicio(request):
    dados = {}

    return render(request, 'desafio/index.html', dados)

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
        
def decompor_arquivo(request):
    arquivo = ModelFormArquivo.objects.get(id = 3)
    print(arquivo.titulo)
    conteudo = open(str(arquivo.arquivo), "r")
    conteudo = conteudo.read()
    conteudo = str.split(conteudo)
    print(conteudo)
    sequencia = 1
    for palavra in conteudo:
        ascII = ''.join(str(ord(c)) for c in palavra)
        print(ascII)
        registro = Caracteres.objects.create(
            arquivo = arquivo, 
            caractere = ascII,
            sequencia = sequencia,
        )   
        sequencia += 1 

        try:
            registro.save()
        except registro:
            pass
        
    dados = {'ok': 'ok'}
    return render(request, 'desafio/enviado.html', dados)


def decompor_caractere(arquivo, caractere, registro):
    pass


class EnvioArquivo(CreateView):
    model = ModelFormArquivo
    form_class = FormularioArquivo
    template_name = 'desafio/enviar_arquivo.html'

    success_url = reverse_lazy('desafio:enviado')