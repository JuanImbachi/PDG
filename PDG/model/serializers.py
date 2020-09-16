from rest_framework import serializers
from .models import DengueRegister
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class DengueRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DengueRegister
        fields = '__all__'
        # extra_kwargs = {}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password':{'required':True, 'write_onlye': True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user
        