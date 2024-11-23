from django.contrib import admin
#Created imports
from apps.cms import models as cms_models

@admin.register(cms_models.Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('slug','title', 'phone', 'email', 'location')
    search_fields = ('title', 'phone', 'email', 'location')
    list_filter = ('title',)
    fieldsets = (
        ("Основная информация", {
            'fields': ('title', 'descriptions', 'icon', 'logo', 'logo_white', )
        }),
        ('Контакты', {
            'fields': ('phone', 'email', 'location')
        }),
        ('Социальные сети', {
            'fields': ('whatsapp', 'instagram', 'youtube', 'facebook')
        }),
    )
    
    
@admin.register(cms_models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title',)
    search_fields = ('title',)
    list_filter = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'descriptions')
        }),
        ('Изображения', {
            'fields': ('imgage1', 'imgage2'),
        }),
    )
