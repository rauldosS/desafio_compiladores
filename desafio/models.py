from django.db import models

# Create your models here.
class ModelFormArquivo(models.Model):
    titulo = models.CharField('Título', max_length=50)
    arquivo = models.FileField('Arquivo', upload_to='arquivos/', blank=False, null=False)
    conteudo = models.TextField('Conteudo', blank=True, null=True)
    conteudo_refatorado = models.TextField('Conteúdo refatorado', blank=True, null=True)
    versao = models.IntegerField('Versao', default=1)

    def __str__(self):
        return f'{self.id} - {self.titulo}'

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'
        ordering = ('id', 'titulo')

class Caracteres(models.Model):
    arquivo = models.ForeignKey(ModelFormArquivo, default='1', on_delete=models.CASCADE)
    asci = models.CharField(max_length=999999)
    ativo = models.BooleanField('Ativo', default=True)
    sequencia = models.IntegerField('Sequencia')
    caractere = models.CharField(max_length=900)
    versao = models.IntegerField('Versão', default=1)

    def __str__(self):
        return f'{self.id} - {self.arquivo} - {self.caractere}'

    class Meta:
        verbose_name = 'Caractere'
        verbose_name_plural = 'Caracteres'
        ordering = ('id', 'caractere')

class Palavras(models.Model):
    arquivo = models.ForeignKey(ModelFormArquivo, default='1', on_delete=models.CASCADE)
    sequencia = models.IntegerField('Sequencia')
    palavra = models.CharField(max_length=900)
    versao = models.IntegerField('Versão', default=1)

    def __str__(self):
        return f'{self.id} - {self.arquivo} - {self.palavra}'

    class Meta:
        verbose_name = 'Palavra'
        verbose_name_plural = 'Palavras'

class Linhas(models.Model):
    arquivo = models.ForeignKey(ModelFormArquivo, default='1', on_delete=models.CASCADE)
    conteudo = models.TextField('Conteúdo')
    linha = models.IntegerField('Linha')
    versao = models.IntegerField('Versão', default=1)

    def __str__(self):
        return f'{self.id} - {self.arquivo} - {self.linha}'

    class Meta:
        verbose_name = 'Linha'
        verbose_name_plural = 'Linhas'
        ordering = ('id', 'linha')

class Numeros(models.Model):
    inteiro = models.IntegerField()
    decimal = models.DecimalField(max_digits=999999, decimal_places=2)
    asci = models.CharField(max_length=999999)

    def __str__(self):
        return f'{self.id} - {self.inteiro}'

    class Meta:
        verbose_name = 'Número'
        verbose_name_plural = 'Números'
        ordering = ('id', 'inteiro')

class Simbolos(models.Model):
    simbolo = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.simbolo}'

    class Meta:
        verbose_name = 'Simbolo'
        verbose_name_plural = 'Simbolo'
        ordering = ('id', 'simbolo')

class Atributos(models.Model):
    atributo = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.atributo}'

    class Meta:
        verbose_name = 'Atributo'
        verbose_name_plural = 'Atributos'
        ordering = ('id', 'atributo')

class AssociacaoSimboloAtributo(models.Model):
    simbolo = models.ForeignKey(Simbolos, on_delete=models.CASCADE)
    atributo = models.ForeignKey(Atributos, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.simbolo} - {self.atributo}'

    class Meta:
        verbose_name = 'Associação símbolo/atributo'
        verbose_name_plural = 'Associação símbolos/atributos'
        ordering = ('id', 'simbolo', 'atributo')