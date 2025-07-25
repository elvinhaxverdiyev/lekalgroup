# Generated by Django 5.2.4 on 2025-07-23 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='background_images', verbose_name='Arxa plan şəkli')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Arxa plan şəkli',
                'verbose_name_plural': 'Arxa plan şəkilləri',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Ad')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='lekalgroupapp.category', verbose_name='Əsas kateqoriya')),
            ],
            options={
                'verbose_name': 'Kateqoriya',
                'verbose_name_plural': 'Kateqoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Ad')),
                ('description', models.TextField(max_length=500, verbose_name='Haqqında')),
                ('price', models.FloatField(verbose_name='Qiymət')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Məhsul aktivliyi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='lekalgroupapp.category', verbose_name='Kateqoriya')),
            ],
            options={
                'verbose_name': 'Məhsul',
                'verbose_name_plural': 'Məhsullar',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Məhsul şəkli')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='lekalgroupapp.product', verbose_name='Məhsul')),
            ],
            options={
                'verbose_name': 'Məhsul şəkli',
                'verbose_name_plural': 'Məhsul şəkilləri',
            },
        ),
    ]
