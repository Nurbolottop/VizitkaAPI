# Generated by Django 5.1.3 on 2024-11-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Slug'),
        ),
    ]
