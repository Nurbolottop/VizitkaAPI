# Generated by Django 5.1.3 on 2024-11-23 15:48

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название сайта')),
                ('descriptions', models.TextField(blank=True, null=True, verbose_name='Информационный текст')),
                ('logo', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo/', verbose_name='Логотип для темного фона')),
                ('icon', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo/', verbose_name='Иконка сайта')),
                ('logo_white', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo/', verbose_name='Логотип для белого фона')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон номер')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Почта')),
                ('location', models.CharField(max_length=255, verbose_name='Адрес')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='WhatsApp URL')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram URL')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='YouTube URL')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook URL')),
            ],
            options={
                'verbose_name': '1) Основная настройка',
                'verbose_name_plural': '1) Основные настройки',
            },
        ),
    ]
