# Generated by Django 2.2 on 2022-03-29 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Tipo', models.CharField(blank=True, max_length=150)),
                ('Empresa', models.CharField(blank=True, max_length=150)),
                ('img', models.URLField(blank=True)),
                ('Cotacao', models.FloatField(blank=True)),
                ('Data_ult_cot', models.DateTimeField()),
                ('Min_52_sem', models.FloatField(blank=True)),
                ('Max_52_sem', models.FloatField(blank=True)),
                ('Vol_med_2m', models.IntegerField(blank=True)),
                ('Valor_de_mercado', models.IntegerField(blank=True)),
                ('Valor_da_firma', models.IntegerField(blank=True)),
                ('Ult_balanco_processado', models.DateTimeField()),
                ('Nro_Acoes', models.IntegerField(blank=True)),
                ('PL', models.IntegerField(blank=True)),
                ('PVP', models.IntegerField(blank=True)),
                ('PEBIT', models.IntegerField(blank=True)),
                ('PSR', models.IntegerField(blank=True)),
                ('PAtivos', models.IntegerField(blank=True)),
                ('PCap_Giro', models.IntegerField(blank=True)),
                ('PAtiv_Circ_Liq', models.IntegerField(blank=True)),
                ('Div_Yield', models.CharField(blank=True, max_length=150)),
                ('EV_EBITDA', models.IntegerField(blank=True)),
                ('EV_EBIT', models.IntegerField(blank=True)),
                ('Cres_Rec_5a', models.CharField(blank=True, max_length=150)),
                ('LPA', models.IntegerField(blank=True)),
                ('VPA', models.IntegerField(blank=True)),
                ('Marg_Bruta', models.CharField(blank=True, max_length=150)),
                ('Marg_EBIT', models.CharField(blank=True, max_length=150)),
                ('Marg_Liquida', models.CharField(blank=True, max_length=150)),
                ('EBIT_Ativo', models.CharField(blank=True, max_length=150)),
                ('ROIC', models.CharField(blank=True, max_length=150)),
                ('ROE', models.CharField(blank=True, max_length=150)),
                ('Liquidez_Corr', models.IntegerField(blank=True)),
                ('Div_Br_Patrim', models.IntegerField(blank=True)),
                ('Giro_Ativos', models.IntegerField(blank=True)),
                ('Ativo', models.IntegerField(blank=True)),
                ('Disponibilidades', models.IntegerField(blank=True)),
                ('Ativo_Circulante', models.IntegerField(blank=True)),
                ('Div_Bruta', models.IntegerField(blank=True)),
                ('Div_Liquida', models.IntegerField(blank=True)),
                ('Patrim_Liq', models.IntegerField(blank=True)),
                ('Receita_Liquida_12m', models.IntegerField(blank=True)),
                ('EBIT_12m', models.IntegerField(blank=True)),
                ('Lucro_Liquido_12m', models.IntegerField(blank=True)),
                ('Receita_Liquida_3m', models.IntegerField(blank=True)),
                ('EBIT_3m', models.IntegerField(blank=True)),
                ('Lucro_Liquido_3m', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubSetore',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=150)),
                ('empresas_sub_setor', models.ManyToManyField(related_name='subsetor_empresa', to='acoes.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Setore',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=150)),
                ('img', models.URLField(blank=True)),
                ('empresas_setor', models.ManyToManyField(related_name='acoes_empresa', to='acoes.Empresa')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='Setor',
            field=models.ManyToManyField(blank=True, to='acoes.Setore'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='Sub_Setor',
            field=models.ManyToManyField(blank=True, to='acoes.SubSetore'),
        ),
        migrations.CreateModel(
            name='Dividendos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Data_com', models.DateTimeField(auto_now_add=True)),
                ('Pagamento', models.DateTimeField(auto_now_add=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('Empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dividendos_acoes', to='acoes.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(blank=True, max_length=150)),
                ('Empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aluguel_acoes', to='acoes.Empresa')),
            ],
        ),
    ]
