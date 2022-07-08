# Generated by Django 4.0.3 on 2022-03-09 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_games', '0002_noticia_alter_user_options_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do serviço')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço do serviço')),
                ('descricao', models.TextField(verbose_name='Descrição do serviço')),
                ('validade', models.IntegerField(choices=[(0, 6), (1, 15), (2, 30)], default=0)),
            ],
            options={
                'verbose_name': 'Servico',
                'verbose_name_plural': 'Servicos',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
