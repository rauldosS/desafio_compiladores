# Generated by Django 3.1.2 on 2020-10-26 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0020_numeros_asci'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='numeros',
            options={'ordering': ('id', 'inteiro'), 'verbose_name': 'Número', 'verbose_name_plural': 'Números'},
        ),
        migrations.RemoveField(
            model_name='numeros',
            name='numero',
        ),
    ]
