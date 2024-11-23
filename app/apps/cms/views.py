from rest_framework import mixins, generics
from rest_framework.response import Response
#Created imports
from apps.cms import models as cms_models
from apps.cms import serializers as cms_serializers
# Create your views here.

class SettingsAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = cms_models.Settings.objects.all()
    serializer_class = cms_serializers.SettingsSerializer
    lookup_field = 'slug'  

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

class AboutAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = cms_models.About.objects.all()
    serializer_class = cms_serializers.AboutSerializer
    lookup_field = 'slug'  

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)