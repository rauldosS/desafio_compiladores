# Generated by Django 3.1.2 on 2020-10-18 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0005_auto_20201018_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='caracteresarquivo',
            name='caractere',
            field=models.CharField(default=1, max_length=999999),
            preserve_default=False,
        ),
    ]