# Generated by Django 5.0.7 on 2024-10-19 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_personalizacao_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalizacao',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]