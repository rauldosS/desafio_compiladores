# Generated by Django 3.1.2 on 2020-10-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0010_auto_20201020_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteres',
            name='versao',
            field=models.IntegerField(default=1, verbose_name='Versão'),
        ),
        migrations.AlterField(
            model_name='linhas',
            name='versao',
            field=models.IntegerField(default=1, verbose_name='Versão'),
        ),
        migrations.AlterField(
            model_name='modelformarquivo',
            name='versao',
            field=models.IntegerField(default=1, verbose_name='Versao'),
        ),
    ]
