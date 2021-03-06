# Generated by Django 3.1.2 on 2020-10-28 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0022_atributos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simbolos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simbolo', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Simbolo',
                'verbose_name_plural': 'Simbolo',
                'ordering': ('id', 'simbolo'),
            },
        ),
        migrations.CreateModel(
            name='AssociacaoSimboloAtributo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atributo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desafio.atributos')),
                ('simbolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desafio.simbolos')),
            ],
            options={
                'verbose_name': 'Associação símbolo/atributo',
                'verbose_name_plural': 'Associação símbolos/atributos',
                'ordering': ('id', 'simbolo', 'atributo'),
            },
        ),
    ]
