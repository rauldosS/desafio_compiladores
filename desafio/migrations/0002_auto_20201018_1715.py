# Generated by Django 3.1.2 on 2020-10-18 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelformarquivo',
            options={'ordering': ('id', 'titulo'), 'verbose_name': 'Arquivo', 'verbose_name_plural': 'Arquivos'},
        ),
    ]
