# Generated by Django 3.1.2 on 2020-10-24 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0015_modelformarquivo_conteudo_refatorado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelformarquivo',
            name='conteudo_refatorado',
            field=models.TextField(blank=True, null=True, verbose_name='Conteúdo refatorado'),
        ),
    ]
