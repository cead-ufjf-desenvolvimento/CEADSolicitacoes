# Generated by Django 4.2.1 on 2023-05-26 12:32

import SolicitacoesApp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolicitacoesApp', '0003_producaodematerial_outro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producaodematerial',
            name='finalidade_gravacao',
        ),
        migrations.AddField(
            model_name='producaodematerial',
            name='finalidade_solicitacao',
            field=models.TextField(blank=True, null=True, validators=[SolicitacoesApp.validators.validate_min_30], verbose_name='Finalidade da Solicitação'),
        ),
    ]