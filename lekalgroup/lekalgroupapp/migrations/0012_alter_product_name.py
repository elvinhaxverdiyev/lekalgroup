# Generated by Django 5.2.4 on 2025-07-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lekalgroupapp', '0011_remove_category_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Ad'),
        ),
    ]
