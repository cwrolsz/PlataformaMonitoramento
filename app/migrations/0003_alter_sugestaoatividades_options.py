# Generated by Django 5.0.7 on 2024-08-01 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_personalizacao_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sugestaoatividades',
            options={'verbose_name': 'Sugestção de atividade', 'verbose_name_plural': 'Sugestões de atividades'},
        ),
    ]