from rest_framework.routers import DefaultRouter
from django.urls import path
#Created imports
from apps.cms import views as cms_views
router = DefaultRouter()


urlpatterns = [
path('settings/<slug:slug>/', cms_views.SettingsAPIView.as_view(), name='cms_settings'),
path('about/<slug:slug>/', cms_views.AboutAPIView.as_view(), name='cms_about'),
]
urlpatterns += router.urls
