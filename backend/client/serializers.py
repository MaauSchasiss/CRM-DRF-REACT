from rest_framework import serializers
from .models import Client

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id', 'name', 'ci', 'email', 'phone', 'address', 'company',
            'source', 'description', 'notes',
            'priority', 'category',
            'create_at', 'updated_at', 'last_purchase',
            'total_purchases', 'products', 'assigned_to', 'created_by'
        )
        read_only_fields = ('create_at', 'updated_at')