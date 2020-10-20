from rest_framework import serializers
from .models import DengueCase

class DengueCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DengueCase
        fields = '__all__'