# Generated by Django 4.2.1 on 2023-06-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolicitacoesApp', '0002_dadospreposto_complemento_viagem_complemento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospreposto',
            name='endereco_numero',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
