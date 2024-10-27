# Generated by Django 5.0.7 on 2024-10-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_personalizacao_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalizacao',
            name='email',
        ),
        migrations.AddField(
            model_name='personalizacao',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
