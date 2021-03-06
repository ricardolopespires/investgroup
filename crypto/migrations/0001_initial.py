# Generated by Django 2.2 on 2022-03-29 21:55

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.CharField(help_text='codigo de indentificação da categoria', max_length=150, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, help_text='A modalidade do crypto ativo', max_length=40, null=True)),
                ('content', models.TextField(null=True)),
                ('market_cap', models.FloatField(null=True)),
                ('market_cap_change_24h', models.FloatField(null=True)),
                ('top_1', models.ImageField(upload_to='crypto/top_1')),
                ('top_2', models.ImageField(upload_to='crypto/top_2')),
                ('top_3', models.ImageField(upload_to='crypto/top_3')),
                ('updated_at', models.DateTimeField(null=True)),
                ('volume_24h', models.FloatField(null=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Cripto',
            fields=[
                ('id', models.CharField(help_text='codigo de indentificação do ativo', max_length=150, primary_key=True, serialize=False, unique=True)),
                ('asset_platform_id', models.CharField(blank=True, help_text='plataforma da cripto ativo', max_length=14, null=True)),
                ('symbol', models.CharField(help_text='Simbolo do cripto ativo', max_length=14)),
                ('name', models.CharField(help_text='Nome do cripto ativo', max_length=14)),
                ('slug', models.SlugField()),
                ('image', models.URLField(help_text='Image do cripto ativo')),
                ('descricao', models.TextField(help_text='Descrição do ativo')),
                ('current_price', models.FloatField(blank=True, default=0, help_text='Valor do Ativo', null=True)),
                ('market_cap', models.FloatField(blank=True, default=0, help_text='valor de mercado', null=True)),
                ('market_cap_rank', models.IntegerField(blank=True, default=0, help_text='A Classificação do crypto ativo no mercado', null=True)),
                ('fully_diluted_valuation', models.FloatField(blank=True, default=0, help_text='Total ativos deluido no mercado', null=True)),
                ('total_volume', models.FloatField(blank=True, default=0, help_text='Fornecimento total', null=True)),
                ('high_24h', models.FloatField(blank=True, default=0, help_text='Valor maximo em 24 horas', null=True)),
                ('low_24h', models.FloatField(blank=True, default=0, help_text='Valor Minimo em 24 horas', null=True)),
                ('price_change_24h', models.FloatField(blank=True, default=0, help_text='Variação do preço de mercado nas 25hr', null=True)),
                ('price_change_percentage_24h', models.FloatField(blank=True, default=0, help_text='Percentual do preço de mercado 24hr', null=True)),
                ('market_cap_change_24h', models.FloatField(blank=True, default=0, help_text='Variação do valor de mercado em 24hr', null=True)),
                ('market_cap_change_percentage_24h', models.FloatField(blank=True, default=0, help_text='Percentual variação do valor mercado 24hr', null=True)),
                ('circulating_supply', models.FloatField(blank=True, default=0, help_text='Ativo em Circulação', null=True)),
                ('total_supply', models.FloatField(blank=True, default=0, help_text='O total de ativos', null=True)),
                ('max_supply', models.FloatField(blank=True, default=0, help_text='O maximo de ativos', null=True)),
                ('ath', models.FloatField(blank=True, default=0, help_text='O valor mais alto do alcançado pelo ativo', null=True)),
                ('ath_change_percentage', models.FloatField(blank=True, default=0, help_text='porcentagem', null=True)),
                ('ath_date', models.DateTimeField(blank=True, help_text='Data da listagem ativo', null=True)),
                ('atl', models.FloatField(blank=True, default=0, help_text='O preço inicial do ativo', null=True)),
                ('atl_change_percentage', models.FloatField(blank=True, default=0, help_text='O porcetagem mais alto', null=True)),
                ('atl_date', models.DateTimeField(blank=True, help_text='Data inicial ativo', null=True)),
                ('roi', models.FloatField(blank=True, default=0, help_text='Retorno sobre Investimento', null=True)),
                ('last_updated', models.DateTimeField(blank=True, help_text='A ultima atualização no ativo', null=True)),
                ('contract_address', models.CharField(help_text='Endereço do Contrato', max_length=14)),
                ('facebook_username', models.CharField(help_text='Página no Facebook', max_length=400)),
                ('twitter_screen_name', models.CharField(help_text='Página no Twitter', max_length=90)),
                ('telegram_channel_identifier', models.CharField(help_text='Página no Telegram', max_length=190)),
                ('blockchain_site', models.CharField(help_text='Página Oficial na Web ', max_length=400)),
                ('official_forum_url', models.CharField(help_text='Página Oficial do forum', max_length=400)),
                ('repos_url', models.CharField(help_text='Repositório no GitHub', max_length=150)),
                ('qr_code', models.ImageField(blank=True, help_text='QR do endereço do contrato ', upload_to='Veiculo/qr_code')),
                ('categoria', models.ManyToManyField(help_text='As categoria do ativo ', to='crypto.Categoria')),
            ],
            options={
                'verbose_name': 'Ativo',
                'verbose_name_plural': 'Ativos',
                'ordering': ['market_cap_rank'],
            },
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.CharField(help_text='codigo de indentificação da plataforma', max_length=150, primary_key=True, serialize=False, unique=True)),
                ('country', models.CharField(blank=True, help_text='Código indetificador da rede', max_length=40, null=True)),
                ('description', models.TextField(blank=True, help_text='Descrição d Exchange ', null=True)),
                ('has_trading_incentive', models.BooleanField(help_text='tem incentivo comercial')),
                ('image', models.ImageField(blank=True, help_text='O simbolo da rede', null=True, upload_to='blockchain/')),
                ('name', models.CharField(help_text='O nome da rede', max_length=40)),
                ('slug', models.SlugField(help_text='Slug')),
                ('trade_volume_24h_btc', models.FloatField()),
                ('trade_volume_24h_btc_normalized', models.FloatField()),
                ('trust_score', models.IntegerField()),
                ('trust_score_rank', models.IntegerField()),
                ('url', models.URLField()),
                ('fee', models.FloatField(blank=True, default=0, help_text='Taxa de transação da exchange', null=True)),
                ('year_established', models.CharField(help_text='Data de inicio da operações da ', max_length=150, null=True)),
                ('cryptos', models.ManyToManyField(related_name='cripto_blockchain', to='crypto.Cripto')),
            ],
            options={
                'verbose_name': 'Exchange',
                'verbose_name_plural': 'Exchanges',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.CharField(help_text='codigo de indentificação do ativo', max_length=150, primary_key=True, serialize=False, unique=True)),
                ('symbol', models.CharField(help_text='Simbolo do cripto ativo', max_length=14)),
                ('name', models.CharField(help_text='Nome do cripto ativo', max_length=14)),
                ('slug', models.SlugField()),
                ('current_price', models.FloatField(blank=True, default=0, help_text='Valor do Ativo', null=True)),
                ('market_cap', models.FloatField(blank=True, default=0, help_text='valor de mercado', null=True)),
                ('total_volume', models.FloatField(blank=True, default=0, help_text='volume', null=True)),
                ('data', models.DateTimeField(help_text='A data historicas')),
                ('facebook_likes', models.FloatField(blank=True, default=0, help_text='Likes dno facebook', null=True)),
                ('twitter_followers', models.FloatField(blank=True, default=0, help_text=' followrs tiwtter', null=True)),
                ('reddit_average_posts_48h', models.FloatField(blank=True, default=0, help_text='reddit average post em 48', null=True)),
                ('reddit_average_comments_48h', models.FloatField(blank=True, default=0, help_text='reddit average comentario em 48', null=True)),
                ('reddit_subscribers', models.FloatField(blank=True, default=0, help_text='inscrito na comunidade', null=True)),
                ('reddit_accounts_active_48h', models.FloatField(blank=True, default=0, help_text='contas ativas', null=True)),
                ('stars', models.IntegerField(blank=True, default=0, help_text='estrelas', null=True)),
                ('subscribers', models.IntegerField(blank=True, default=0, help_text='assinantes', null=True)),
                ('total_issues', models.IntegerField(blank=True, default=0, help_text='questões totais', null=True)),
                ('closed_issues', models.IntegerField(blank=True, default=0, help_text='questões encerradas"', null=True)),
                ('pull_requests_merged', models.IntegerField(blank=True, default=0, help_text='solicitações pull mescladas', null=True)),
                ('pull_request_contributors', models.IntegerField(blank=True, default=0, help_text='solicitação dos contribuidores', null=True)),
                ('views', models.IntegerField(default=0, help_text='Quantidade de atualização diaria ', null=True)),
            ],
            options={
                'verbose_name': 'Historico',
                'verbose_name_plural': 'Históricos',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.CharField(help_text='Código do investimento', max_length=150, primary_key=True, serialize=False, unique=True)),
                ('deposito', models.IntegerField(blank=True, default=0, help_text='Quantidade de deposito', null=True)),
                ('retirada', models.IntegerField(blank=True, default=0, help_text='Quantidade de retirada', null=True)),
                ('preco', models.FloatField(blank=True, default=0, help_text='O preço pago por unidade', null=True)),
                ('quantidade', models.FloatField(blank=True, default=0, help_text='Quantidade de moeda', null=True)),
                ('media', models.FloatField(blank=True, default=0, help_text='Media do valor pago', null=True)),
                ('retorno', models.FloatField(blank=True, default=0, help_text='O valor do retorno', null=True)),
                ('taxa_retorno', models.FloatField(blank=True, default=0, help_text='O valor da porcentagem do investimento', null=True)),
                ('rating', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('inicio', models.DateTimeField(auto_now_add=True, help_text='A data do inicio do investimento')),
                ('final', models.DateTimeField(blank=True, help_text='A data final do investimento', null=True)),
                ('duracao_total', models.DurationField(blank=True, default=datetime.timedelta(0), null=True)),
                ('total', models.FloatField(blank=True, default=0, help_text='O valor total do investimento', null=True)),
                ('crypto', models.ForeignKey(help_text='A moeda do investimento', on_delete=django.db.models.deletion.CASCADE, related_name='crypto', to='crypto.Cripto')),
                ('investidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_investimento', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Investimento',
                'verbose_name_plural': 'Investimentos',
                'ordering': ['-inicio'],
            },
        ),
        migrations.CreateModel(
            name='Price_percentage_change',
            fields=[
                ('id', models.CharField(help_text='codigo de indentificação do ativo', max_length=150, primary_key=True, serialize=False, unique=True)),
                ('periodo', models.DateTimeField()),
                ('data', models.DateTimeField()),
                ('p_30', models.FloatField(help_text='Porcetagem do periodo de 30 dias')),
                ('p_90', models.FloatField(help_text='Porcetagem do periodo de 90 dias')),
                ('p_180', models.FloatField(help_text='Porcetagem do periodo de 180 dias')),
                ('p_1', models.FloatField(help_text='Porcetagem do periodo de 1 Ano')),
            ],
            options={
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Roi',
            fields=[
                ('id', models.CharField(help_text='codigo de indentificação do ativo', max_length=150, primary_key=True, serialize=False, unique=True)),
                ('symbol', models.CharField(help_text='Simbolo do cripto ativo', max_length=14)),
                ('name', models.CharField(help_text='Nome do cripto ativo', max_length=14)),
                ('slug', models.SlugField()),
                ('current_price', models.FloatField(blank=True, default=0, help_text='Valor do Ativo', null=True)),
                ('market_cap', models.FloatField(blank=True, default=0, help_text='valor de mercado', null=True)),
                ('data', models.DateTimeField(auto_now_add=True, help_text='A data historica')),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.CharField(help_text='codigo de indentificação da plataforma', max_length=150, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(help_text='O nome da rede', max_length=40)),
                ('slug', models.SlugField()),
                ('simbolo', models.CharField(help_text='O simbolo da rede', max_length=90)),
                ('token_address', models.CharField(blank=True, help_text='Endereço do token', max_length=90, null=True)),
                ('qr_code', models.ImageField(blank=True, help_text='QR code de autorização do veiculo', null=True, upload_to='token_address/qr_code')),
                ('cryptos', models.ManyToManyField(related_name='cripto_plataforma', to='crypto.Cripto')),
            ],
            options={
                'verbose_name': 'Plataforma',
                'verbose_name_plural': 'Plataformas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.CharField(help_text='Código do retorno movimentação', max_length=150, primary_key=True, serialize=False, unique=True)),
                ('tipo', models.CharField(choices=[('ótimo', 'Ótimo'), ('bom', 'Bom'), ('regular', 'Regular'), ('péssimo', 'Péssimo')], default='bom', help_text='Status da movimentação', max_length=90)),
                ('status', models.CharField(choices=[('deposito', 'Deposito'), ('retirada', 'Retirada')], default='deposito', help_text='O tipo de movimentação', max_length=90)),
                ('data', models.DateTimeField(help_text='A data do valor do retorno')),
                ('valor', models.FloatField(default=0, help_text='O valor do movimentação')),
                ('quantidade', models.FloatField(default=0, help_text='Quantidade de moeda')),
                ('preco', models.FloatField(default=0, help_text='O preço pago por unidade')),
                ('retorno', models.FloatField(default=0, help_text='O valor do retorno')),
                ('porcentagem', models.FloatField(default=0, help_text='Porcetagem do investimento')),
                ('total', models.FloatField(default=0, help_text='O valor total do retorno do movimentação')),
                ('saldo', models.FloatField(default=0, help_text='Saldo do retorno do movimentação')),
                ('crypto', models.ForeignKey(help_text='A moeda do investimento', on_delete=django.db.models.deletion.CASCADE, related_name='aporte_crypto', to='crypto.Cripto')),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aporte_blockchain', to='crypto.Exchange')),
                ('investidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_aporte', to=settings.AUTH_USER_MODEL)),
                ('investimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aporte_movimentação', to='crypto.Investimento')),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
                'ordering': ['-data'],
            },
        ),
        migrations.AddField(
            model_name='categoria',
            name='cryptos',
            field=models.ManyToManyField(related_name='cripto_tags', to='crypto.Cripto'),
        ),
    ]
