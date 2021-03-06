# Generated by Django 3.1.2 on 2020-10-18 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0004_modelformarquivo_conteudo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelformarquivo',
            name='arquivo',
            field=models.FileField(upload_to='arquivos/', verbose_name='Arquivo'),
        ),
        migrations.AlterField(
            model_name='modelformarquivo',
            name='conteudo',
            field=models.CharField(blank=True, max_length=999999, null=True, verbose_name='Conteudo'),
        ),
        migrations.AlterField(
            model_name='modelformarquivo',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='Título'),
        ),
        migrations.CreateModel(
            name='CaracteresArquivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filtro', models.CharField(choices=[('AT', 'Ativo'), ('IN', 'Inativo')], max_length=2)),
                ('arquivo', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='desafio.modelformarquivo')),
            ],
        ),
    ]
