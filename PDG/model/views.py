from django.shortcuts import render
from rest_framework import viewsets
from .models import DengueRegister
from .serializers import DengueRegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

class DengueRegisterViewSet(viewsets.ModelViewSet):
    queryset = DengueRegister.objects.all()
    serializer_class = DengueRegisterSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    @action(methods=['POST'], detail=True)
    def registerDengueCase(self, request):
        print('register')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


