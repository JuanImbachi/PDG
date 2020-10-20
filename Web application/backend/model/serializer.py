from rest_framework import serializers
from .models import DengueCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class DengueCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DengueCase
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'required':True, 'write_only':True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user