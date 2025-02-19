from rest_framework import serializers
from .models import leads

class LeadsSerializers(serializers.ModelSerializer):
    class Meta:
        model = leads
        fields = ('name', 'ci', 'email', 'phone', 'adrees', 'source', 'product_interest', 'description',
                'status', 'priority', 'created_at', 'updated_at', 'last_contact', 'notes') 
        read_only_fields = ('created_at', 'updated_at')