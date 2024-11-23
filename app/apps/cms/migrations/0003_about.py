# Generated by Django 5.1.3 on 2024-11-23 18:46

import ckeditor.fields
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_settings_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgage1', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='about_image/', verbose_name='Первая фотография о нас')),
                ('imgage2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='about_image/', verbose_name='Первая фотография о нас')),
                ('title', models.CharField(max_length=255, verbose_name='О нас')),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': '2) Добавление информации о нас',
                'verbose_name_plural': '2) Добавление информации о нас',
            },
        ),
    ]