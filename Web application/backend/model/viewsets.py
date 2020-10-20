from rest_framework import viewsets
from .models import DengueCase
from .serializer import DengueCaseSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

class DengueCaseViewSet(viewsets.ModelViewSet):
    queryset = DengueCase.objects.all()
    serializer_class = DengueCaseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)