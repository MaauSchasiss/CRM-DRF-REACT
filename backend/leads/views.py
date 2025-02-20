from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Leads
from .serializers import LeadsSerializers


# Create your views here.
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializers  
    permission_classes = [permissions.AllowAny]