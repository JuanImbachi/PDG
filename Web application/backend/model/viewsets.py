from rest_framework import viewsets
from .models import DengueCase
from .serializer import DengueCaseSerializer

class DengueCaseViewSet(viewsets.ModelViewSet):
    queryset = DengueCase.objects.all()
    serializer_class = DengueCaseSerializer