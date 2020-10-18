from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import ModelFormArquivo
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
        
class EnvioArquivo(CreateView):
    model = ModelFormArquivo
    form_class = FormularioArquivo
    template_name = 'desafio/enviar_arquivo.html'

    success_url = reverse_lazy('desafio:enviado')