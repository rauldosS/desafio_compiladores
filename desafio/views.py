from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .models import ModelFormArquivo, Caracteres, Linhas
from .forms import FormularioArquivo
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q
import json
from django.core.files.base import ContentFile

# Create your views here.
class EnvioArquivo(CreateView):
    model = ModelFormArquivo
    form_class = FormularioArquivo
    template_name = 'desafio/enviar_arquivo.html'

    success_url = reverse_lazy('desafio:enviado')

def inicio(request):
    arquivos = ModelFormArquivo.objects.all()

    return render(request, 'desafio/index.html', {'arquivos': arquivos})

def enviar_arquivo(request):
    if request.method == 'POST':
        form = ModelFormArquivo(request.POST, request.FILES)
        if form.is_valid():
            # salvar arquivo
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormArquivo()
    return render(request, 'enviar_arquivo.html', {'form': form})

def arquivo(request, id=1):
    arquivo_modelo = ModelFormArquivo.objects.get(id=id)
    caracteres = Caracteres.objects.filter(arquivo=arquivo_modelo, ativo=True).order_by('sequencia')
    caracteres_removidos = Caracteres.objects.filter(arquivo=arquivo_modelo, ativo=False).order_by('sequencia')
    linhas = Linhas.objects.filter(arquivo=arquivo_modelo).order_by('linha')

    arquivo = open(str(arquivo_modelo.arquivo), 'r', encoding='utf-8-sig')
    conteudo = arquivo.read()
    arquivo.close()

    dados = {
        'arquivo': arquivo_modelo,
        'conteudo': conteudo,
        'caracteres': caracteres,
        'linhas': linhas,
        'caracteres_removidos': caracteres_removidos
    }

    return render(request, 'desafio/arquivo/arquivo.html', dados)

def decompor_arquivo(request, id=1):
    arquivo_modelo = ModelFormArquivo.objects.get(id=id)
    caracteres_removidos = Caracteres.objects.filter(arquivo=arquivo_modelo, ativo=False).order_by('sequencia')
    
    arquivo = open(str(arquivo_modelo.arquivo), 'r', encoding='utf-8-sig')
    conteudo = arquivo.read()
    arquivo.close()

    atualizar_arquivo(id, conteudo, arquivo_modelo.versao + 1)
    decompor_caracteres(arquivo_modelo, conteudo, caracteres_removidos)

    atualizar_linhas(arquivo_modelo)

    return redirect('desafio:arquivo', id=arquivo_modelo.id)

def atualizar_arquivo(id, conteudo, versao):
    try:
        registro = ModelFormArquivo.objects.get(id=id)

        registro.conteudo = conteudo,
        registro.versao = versao

        registro.save()
    except:
        print('Erro ao atualizar arquivo')

def decompor_caracteres(arquivo, conteudo, caracteres_removidos):
    caracteres_arquivo_false = []
    for caractere in Caracteres.objects.filter(arquivo=arquivo, ativo=False):
        print(f'Decompondo caractere: { caractere }')
        caracteres_arquivo_false.append([caractere.sequencia, str(caractere.palavra)])

    atualizar_caractere(Caracteres.objects.filter(arquivo=arquivo))

    sequencia = 1
    for palavra in str.split(conteudo):
        print(f'Decompondo palavra: { palavra }')
        ativo = True

        for caractere in caracteres_arquivo_false:
            if (palavra in caractere[1] and sequencia == caractere[0]):
                ativo = False

        ascII = ''.join(str(ord(c)) for c in palavra)
        registro = Caracteres.objects.create(
            arquivo = arquivo, 
            caractere = ascII,
            sequencia = sequencia,
            palavra = palavra,
            ativo = ativo
        )
        sequencia += 1

    if caracteres_removidos:
        remover_caractere(caracteres_removidos, arquivo)
    
    # Deletar caracteres da versão 2
    Caracteres.objects.filter(arquivo=arquivo, caractere='atualizado').delete()

def atualizar_caractere(objetos):
    for caractere in objetos:
        print(f'Atualizando arquivo: { caractere }')
        caractere.caractere = 'atualizado'
        caractere.save()

def remover_caractere(caracteres, arquivo):
    caracteres_removidos = []

    for remover in caracteres:
        caractere = Caracteres.objects.get(~Q(id=remover[0]), arquivo, sequencia=remover[1])
        caracteres_removidos.append(caractere)

    for caractere in caracteres_removidos:
        print(f'Removendo caractere: { caractere }')
        caractere.ativo = False
        print(caractere.save())

def atualizar_linhas(arquivo):
    Linhas.objects.filter(arquivo=arquivo).delete()

    with open(str(arquivo.arquivo), 'r', errors='replace', encoding='utf-8-sig') as a:
        linhas = a.readlines()

        contagem_linha = 1
        for linha in linhas:
            print(f'Atualizando linhas: { linha }')
            # print(f'Linha {contagem_linha}: {linha.strip()}')

            registro = Linhas.objects.create(
                arquivo=arquivo,
                conteudo=linha.strip(),
                linha=contagem_linha
            )

            contagem_linha += 1

            registro.save()

def atualizar_arquivo_completo(request):
    if request.method == "POST":
        json_arquivo = json.loads(request.POST.get('arquivo', ''))
        arquivo_modelo = ModelFormArquivo.objects.get(id=int(json_arquivo['id']))
        versao = arquivo_modelo.versao + 1
        caracteres_removidos = json_arquivo['chips_selecionados']

        # Atualiza caracteres da nova versão
        arquivo = open(str(arquivo_modelo.arquivo), 'r', encoding='utf-8-sig')
        conteudo = arquivo.read()
        arquivo.close()

        decompor_caracteres(arquivo_modelo, conteudo, caracteres_removidos)
        # atualizar_linhas(arquivo_modelo)

        # Atualiza arquivos
        # atualizar_arquivo(int(json_arquivo['id'], json_arquivo['conteudo'], versao))

        return redirect('desafio:arquivo', id=arquivo_modelo.id)
    

def gerar_arquivo(arquivo):
    pass

def arquivos_enviados(request):
    arquivos = ModelFormArquivo.objects.all()

    return render(request, 'desafio/arquivos_enviados.html', {'arquivos': arquivos})