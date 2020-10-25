from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .models import ModelFormArquivo, Caracteres, Linhas, Palavras
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
    palavras = Palavras.objects.filter(arquivo=arquivo_modelo).order_by('sequencia')

    arquivo = open(str(arquivo_modelo.arquivo), 'r', encoding='utf-8-sig')
    conteudo = arquivo.read()
    arquivo.close()

    dados = {
        'arquivo': arquivo_modelo,
        'conteudo': conteudo,
        'caracteres': caracteres,
        'linhas': linhas,
        'palavras': palavras,
        'caracteres_removidos': caracteres_removidos,
        'referencias_cruzadas': referencias_cruzadas(arquivo_modelo)
    }

    return render(request, 'desafio/arquivo/arquivo.html', dados)

def decompor_arquivo(request, id=1):
    arquivo_modelo = ModelFormArquivo.objects.get(id=id)

    print('-'*50)
    print(f'Decompondo arquivo { arquivo_modelo.titulo }')
    print('-'*50)
    
    arquivo = open(str(arquivo_modelo.arquivo), 'r', encoding='utf-8-sig')
    conteudo = arquivo.read()
    arquivo.close()

    atualizar_arquivo(id, conteudo, arquivo_modelo.versao + 1)
    decompor_caracteres(arquivo_modelo, conteudo, [])
    separar_palavras(arquivo_modelo, conteudo)

    atualizar_linhas(arquivo_modelo)

    return redirect('desafio:arquivo', id=arquivo_modelo.id)

def atualizar_arquivo(id, conteudo, versao):
    try:
        registro = ModelFormArquivo.objects.get(id=id)

        print('-'*50)
        print(f'Atualizando arquivo { registro.titulo }')
        print('-'*50)

        registro.conteudo_refatorado = conteudo,
        registro.versao = versao

        registro.save()
    except:
        print('Erro ao atualizar arquivo')

def decompor_caracteres(arquivo, conteudo, caracteres_removidos):
    for caractere in Caracteres.objects.filter(arquivo=arquivo, ativo=False):
        print(caractere)
        caracteres_removidos.append(caractere.sequencia)
            
    atualizar_caractere(Caracteres.objects.filter(arquivo=arquivo))

    print('-'*50)
    print(f'Decompondo caracteres do arquivo { arquivo.titulo }')
    print('-'*50)

    sequencia = 1
    for caractere in conteudo:
        print(f'Decompondo caractere: { caractere }')
        ativo = True

        ascII = ''.join(str(ord(c)) for c in caractere)
        print(f'Caractere \'{ caractere }\' convertido em ASCII: { ascII }')

        registro = Caracteres.objects.create(
            arquivo = arquivo, 
            asci = ascII,
            sequencia = sequencia,
            caractere = caractere,
            ativo = ativo
        )
        sequencia += 1

    # Deletar caracteres da versões anteriores
    Caracteres.objects.filter(arquivo=arquivo, caractere='atualizado').delete()
        
    remover_caractere_selecionados(
        Caracteres.objects.filter(arquivo=arquivo),
        caracteres_removidos
    )

def separar_palavras(arquivo, conteudo):
    print('-'*50)
    print(f'Separando palavras do arquivo { arquivo.titulo }')
    print('-'*50)

    atualizar_palavra(Palavras.objects.filter(arquivo=arquivo))

    sequencia = 1
    for palavra in str.split(conteudo):
        print(f'Separando palavra: { palavra }')

        ascII = ''.join(str(ord(c)) for c in palavra)
        registro = Palavras.objects.create(
            arquivo = arquivo, 
            sequencia = sequencia,
            palavra = palavra
        )
        sequencia += 1
    
    # Deletar palavras de versões anteriores
    Palavras.objects.filter(arquivo=arquivo, palavra='atualizado').delete()

def atualizar_caractere(objetos):
    print('-'*50)
    print('Atualizando caracteres do arquivo')
    print('-'*50)
    for caractere in objetos:
        print(f'Atualizando arquivo: { caractere }')
        caractere.caractere = 'atualizado'
        caractere.save()

def atualizar_palavra(objetos):
    print('-'*50)
    print('Atualizando palavras do arquivo')
    print('-'*50)
    for palavra in objetos:
        print(f'Atualizando arquivo: { palavra }')
        palavra.palavra = 'atualizado'
        palavra.save()

def remover_caractere_selecionados(caracteres, caracteres_selecionados):
    print('-'*50)
    print(f'Caracteres que serão desativados: { caracteres_selecionados }')
    print('-'*50)
    for caractere in caracteres:
        if caractere.sequencia in caracteres_selecionados:
            caractere.ativo = False
            caractere.save()
            print(f'Caractere \'{ caractere.caractere }\' desativado')

def remover_caractere(caracteres, arquivo):
    print('-'*50)
    print(f'Desativando caracteres do arquivo { arquivo.titulo }')
    print('-'*50)
    caracteres_removidos = []

    for remover in caracteres:
        caractere = Caracteres.objects.get(~Q(id=remover[0]), arquivo, sequencia=remover[1])
        caracteres_removidos.append(caractere)

    for caractere in caracteres_removidos:
        print(f'Removendo caractere: { caractere }')
        caractere.ativo = False
        print(caractere.save())

def atualizar_linhas(arquivo):
    print('-'*50)
    print(f'Atualizando linhas do arquivo { arquivo.titulo }')
    print('-'*50)
    Linhas.objects.filter(arquivo=arquivo).delete()

    with open(str(arquivo.arquivo), 'r', errors='replace', encoding='utf-8-sig') as a:
        linhas = a.readlines()

        contagem_linha = 1
        for linha in linhas:
            print(f'Atualizando linha {contagem_linha}: {linha.strip()}')

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
        chips_selecionados = json_arquivo['chips_selecionados']

        # Atualiza caracteres da nova versão
        arquivo = open(str(arquivo_modelo.arquivo), 'r', encoding='utf-8-sig')
        conteudo = arquivo.read()
        arquivo.close()

        decompor_caracteres(arquivo_modelo, conteudo, chips_selecionados)
        atualizar_linhas(arquivo_modelo)

        return redirect('desafio:arquivo', id=arquivo_modelo.id)
    
def refatorar_conteudo(arquivo):
    pass

def referencias_cruzadas(arquivo):
    referencias = {}

    for palavra in Palavras.objects.filter(arquivo=arquivo).order_by('palavra'):
        referencias.update({palavra.palavra: []})

    # Se a referência contem alguma palavra desta linha, adiciona a linha ao array de referência
    for referencia, linhas in referencias.items():
        sequencia = 1
        for linha in Linhas.objects.filter(arquivo=arquivo).order_by('linha'):
            sequencia = linha.linha
            palavras_linha = (str.split(linha.conteudo))

            if referencia in palavras_linha:
                referencias[referencia].append(sequencia)
    
    print(referencias)

    return referencias