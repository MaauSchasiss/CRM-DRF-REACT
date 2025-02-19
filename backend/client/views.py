from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Client
from .serializers import ClienteSerializer


# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClienteSerializer  
    permission_classes = [permissions.AllowAny]