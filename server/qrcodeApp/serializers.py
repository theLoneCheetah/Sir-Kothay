from rest_framework import serializers
from .models import QRCode


class QRCodeSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    qr_url = serializers.SerializerMethodField()
    
    class Meta:
        model = QRCode
        fields = ['id', 'user', 'user_email', 'user_username', 'image', 'qr_url', 'generated_at']
        read_only_fields = ['id', 'user', 'generated_at']
    
    def get_qr_url(self, obj):
        return obj.get_qr_url
