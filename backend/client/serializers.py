from rest_framework import serializers
from .models import Client

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id','name','ci','email','phone','adrees')
        read_only_fields= ('create_at',)