# Generated by Django 4.2.1 on 2023-06-05 15:59

import SolicitacoesApp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipamentoProducaoDeMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServicoProducaoDeMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProducaoDeMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outro', models.CharField(blank=True, max_length=100, null=True)),
                ('professor_responsavel', models.CharField(max_length=100, validators=[SolicitacoesApp.validators.validate_nome_completo], verbose_name='Professor Responsável')),
                ('setor_curso', models.CharField(max_length=100, verbose_name='Setor Curso')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('data_agendamento', models.DateField(blank=True, null=True, validators=[SolicitacoesApp.validators.validate_data_futuro], verbose_name='Data de Agendamento')),
                ('horario_agendamento', models.TimeField(blank=True, null=True, validators=[SolicitacoesApp.validators.validate_horario_agendamento], verbose_name='Horário de Agendamento')),
                ('duracao_estimada', models.CharField(blank=True, max_length=20, null=True, verbose_name='Duração da Estimada')),
                ('data_entrega_material', models.DateField(validators=[SolicitacoesApp.validators.validate_data_futuro], verbose_name='Data de Entrega do Material')),
                ('finalidade_solicitacao', models.TextField(validators=[SolicitacoesApp.validators.validate_min_30], verbose_name='Finalidade da Solicitação')),
                ('arte_pronta', models.FileField(blank=True, null=True, upload_to='arte_pronta/', verbose_name='Arte para produção de material')),
                ('detalhes_arte', models.TextField(blank=True, null=True, verbose_name='Descreva sua arte aqui')),
                ('equipe_cead', models.BooleanField(choices=[(False, 'Não, iremos utilizar a nossa própria equipe'), (True, 'Sim, precisaremos da equipe do CEAD')], default=False, verbose_name='Precisará de nossa equipe de cinegrafistas?')),
                ('numero_participantes', models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], null=True, verbose_name='Número de participantes')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('equipamentos', models.ManyToManyField(blank=True, to='SolicitacoesApp.equipamentoproducaodematerial')),
                ('servicos', models.ManyToManyField(blank=True, to='SolicitacoesApp.servicoproducaodematerial', verbose_name='Serviços')),
            ],
        ),
    ]
