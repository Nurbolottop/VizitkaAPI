# accounts/serializers.py

from rest_framework import serializers
from apps.users import models as users_models


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users_models.CustomUser
        fields = ('id', 'email', 'first_name', 'last_name')
