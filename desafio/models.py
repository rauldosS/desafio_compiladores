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
        verbose_name = 'Caractere'
        verbose_name_plural = 'Caracteres'

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
    numero = models.CharField(max_length=999999)
    inteiro = models.IntegerField()
    decimal = models.DecimalField(max_digits=999999, decimal_places=2)
    asci = models.CharField(max_length=999999)

    def __str__(self):
        return f'{self.id} - {self.numero} - {self.inteiro}'

    class Meta:
        verbose_name = 'Número'
        verbose_name_plural = 'Números'
        ordering = ('id', 'numero')
