from django import forms
from desafio.models import ModelFormArquivo
import re

class FormularioArquivo(forms.ModelForm):
    """ Formulário para salvar arquivo na base de dados

    Variables:

        - password1: senha
        - password2: verificação de senha

    """

    class Meta:
        model = ModelFormArquivo
        fields = ('titulo', 'arquivo')
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe o título do arquivo'
                }
            ),
            'arquivo': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                    'type': 'file',
                }
            ),
        }

    def save(self, commit=True):
        arquivo = super().save(commit = False)
        
        if commit:
            arquivo.save()

        return arquivo