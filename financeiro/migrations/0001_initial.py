# Generated by Django 2.2 on 2022-03-29 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.CharField(help_text='Numero indentificador da movimentação', max_length=150, primary_key=True, serialize=False)),
                ('institucao', models.CharField(blank=True, help_text='A pessoa que faz o pagamento', max_length=400)),
                ('data', models.DateTimeField(help_text='A data do movimento')),
                ('descricao', models.TextField(help_text='Descrição do movimento')),
                ('tipo', models.CharField(choices=[('-', '-'), ('D', 'Debito'), ('C', 'Cretido')], default='-', help_text='O tipo do movimento bancario', max_length=150)),
                ('modelo', models.CharField(choices=[('-', '-'), ('dinheiro', 'Dinheiro'), ('ações', 'Ações'), ('crypto', 'Crypto'), ('imobiliario', 'Imobiliario')], default='-', help_text='O tipo do movimento bancario', max_length=150)),
                ('valor', models.DecimalField(decimal_places=2, help_text='O valor do movimento', max_digits=10)),
                ('saldo', models.DecimalField(decimal_places=2, help_text='O valor que ficou de saldo na conta', max_digits=10)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sindico_movimentação', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
                'ordering': ['valor'],
            },
        ),
        migrations.CreateModel(
            name='Financeiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinheiro', models.DecimalField(decimal_places=2, default=0, help_text='Valor do capital em dinheiro', max_digits=10)),
                ('acoes', models.DecimalField(decimal_places=2, default=0, help_text='Valor do capital em ações', max_digits=10)),
                ('crypto', models.DecimalField(decimal_places=2, default=0, help_text='Valor do capital em crypto moedas', max_digits=10)),
                ('imobiliario', models.DecimalField(decimal_places=2, default=0, help_text='Valor do capital em fundos imobiliario', max_digits=10)),
                ('capital', models.DecimalField(decimal_places=2, default=0, help_text='Valor total do capital', max_digits=10)),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Data da ultima atualização do Financeiro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resets', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
