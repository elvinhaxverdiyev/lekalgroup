# Generated by Django 5.2.4 on 2025-07-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lekalgroupapp', '0006_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Əməkdaş aktivliyi'),
        ),
    ]
