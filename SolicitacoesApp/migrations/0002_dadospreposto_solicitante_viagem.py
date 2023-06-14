# Generated by Django 4.2.1 on 2023-06-14 13:41

import SolicitacoesApp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolicitacoesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosPreposto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, validators=[SolicitacoesApp.validators.validate_cpf])),
                ('rg', models.CharField(max_length=20)),
                ('filiacao_mae', models.CharField(max_length=100)),
                ('filiacao_pai', models.CharField(blank=True, max_length=100)),
                ('agencia', models.CharField(max_length=10)),
                ('conta_corrente', models.CharField(max_length=20)),
                ('banco', models.CharField(max_length=100)),
                ('endereco_logradouro', models.CharField(max_length=200)),
                ('endereco_numero', models.CharField(max_length=10)),
                ('endereco_bairro', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=100)),
                ('coordenador', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localidade_logradouro', models.CharField(max_length=200)),
                ('localidade_numero', models.CharField(max_length=10)),
                ('localidade_bairro', models.CharField(max_length=100)),
                ('data_saida', models.DateField(validators=[SolicitacoesApp.validators.validate_data_futuro])),
                ('data_retorno', models.DateField(validators=[SolicitacoesApp.validators.validate_data_futuro])),
                ('objetivo', models.CharField(max_length=200)),
                ('outras_informacoes', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
