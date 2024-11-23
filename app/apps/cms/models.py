from django.db import models
from django.utils.text import slugify
from django_resized.forms import ResizedImageField
from ckeditor.fields import RichTextField

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название сайта")
    descriptions = models.TextField(verbose_name="Информационный текст", blank=True, null=True)
    logo = ResizedImageField(force_format="WEBP", quality=100, upload_to="logo/", verbose_name="Логотип для темного фона")
    icon = ResizedImageField(force_format="WEBP", quality=100, upload_to="logo/", verbose_name="Иконка сайта")
    logo_white = ResizedImageField(force_format="WEBP", quality=100, upload_to="logo/", verbose_name="Логотип для белого фона")
    phone = models.CharField(max_length=255, verbose_name='Телефон номер')
    email = models.EmailField(max_length=255, verbose_name='Почта', blank=True, null=True)
    location = models.CharField(max_length=255, verbose_name='Адрес')
    whatsapp = models.URLField(verbose_name='WhatsApp URL', blank=True, null=True)
    instagram = models.URLField(verbose_name='Instagram URL', blank=True, null=True)
    youtube = models.URLField(verbose_name='YouTube URL', blank=True, null=True)
    facebook = models.URLField(verbose_name='Facebook URL', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Slug")  # Добавлено поле slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # Генерация slug на основе title всегда при сохранении
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "1) Основная настройка"
        verbose_name_plural = "1) Основные настройки"


class About(models.Model):
    imgage1 = ResizedImageField(force_format="WEBP", quality=100,upload_to='about_image/',verbose_name="Первая фотография о нас",blank=True, null=True)
    imgage2 = ResizedImageField(force_format="WEBP", quality=100,upload_to='about_image/',verbose_name="Первая фотография о нас",blank=True, null=True)
    title = models.CharField(max_length=255,verbose_name="О нас")
    descriptions = RichTextField(verbose_name="Описание")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Slug")  # Добавлено поле slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # Генерация slug на основе title всегда при сохранении
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "2) Добавление информации о нас"
        verbose_name_plural = "2) Добавление информации о нас"