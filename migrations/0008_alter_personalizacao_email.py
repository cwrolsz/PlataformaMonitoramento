# Generated by Django 5.0.7 on 2024-10-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_personalizacao_email_personalizacao_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalizacao',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
