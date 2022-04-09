# Generated by Django 2.2 on 2022-03-29 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0004_auto_20220329_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='facebook_likes',
            field=models.FloatField(blank=True, default=0, help_text='Likes dno facebook', null=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='reddit_accounts_active_48h',
            field=models.FloatField(blank=True, default=0, help_text='contas ativas', null=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='reddit_average_comments_48h',
            field=models.FloatField(blank=True, default=0, help_text='reddit average comentario em 48', null=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='reddit_average_posts_48h',
            field=models.FloatField(blank=True, default=0, help_text='reddit average post em 48', null=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='reddit_subscribers',
            field=models.FloatField(blank=True, default=0, help_text='inscrito na comunidade', null=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='twitter_followers',
            field=models.FloatField(blank=True, default=0, help_text=' followrs tiwtter', null=True),
        ),
    ]
