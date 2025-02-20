from rest_framework import serializers
from .models import Leads

class LeadsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = (
            'name', 'ci', 'email', 'phone', 'adrees', 'company',
            'source', 'product_interest', 'description',
            'status', 'priority', 'created_at', 'updated_at',
            'last_contact', 'notes',
            'assigned_to', 'created_by', 'client', 'category'
        )
        read_only_fields = ('created_at', 'updated_at')