from rest_framework import serializers
from .models import Hall

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'updated_at']
