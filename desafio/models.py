from django.db import models

# Create your models here.
class ModelFormArquivo(models.Model):
    titulo = models.CharField('Título', max_length=50)
    arquivo = models.FileField('Arquivo', upload_to='arquivos/', blank=False, null=False)
    conteudo = models.CharField('Conteudo', max_length=999999, blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.titulo}'

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'
        ordering = ('id', 'titulo')

class Caracteres(models.Model):
    arquivo = models.ForeignKey(ModelFormArquivo, default='1', on_delete=models.CASCADE)
    caractere = models.CharField(max_length=999999)
    ativo = models.BooleanField('Ativo', default=True)