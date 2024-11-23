from rest_framework import serializers
from apps.cms import models as cms_models


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cms_models.Settings
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = cms_models.About
        fields = '__all__'