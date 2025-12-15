from rest_framework import serializers
from .models import BroadcastMessage


class BroadcastMessageSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = BroadcastMessage
        fields = ['id', 'user', 'user_email', 'user_username', 'message', 'active']
        read_only_fields = ['id', 'user']
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
