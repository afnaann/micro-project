from rest_framework import serializers

from .models import Auther


class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auther
        fields = ['name','age']
    