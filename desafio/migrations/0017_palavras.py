# Generated by Django 3.1.2 on 2020-10-24 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0016_auto_20201024_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palavras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequencia', models.IntegerField(verbose_name='Sequencia')),
                ('palavra', models.CharField(max_length=900)),
                ('versao', models.IntegerField(default=1, verbose_name='Versão')),
                ('arquivo', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='desafio.modelformarquivo')),
            ],
            options={
                'verbose_name': 'Caractere',
                'verbose_name_plural': 'Caracteres',
                'ordering': ('id', 'sequencia', 'palavra'),
            },
        ),
    ]
