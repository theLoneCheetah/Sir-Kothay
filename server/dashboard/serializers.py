from rest_framework import serializers
from .models import UserDetails
from authApp.models import CustomUser


class UserDetailsSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    profile_image_url = serializers.SerializerMethodField()
    slug = serializers.CharField(read_only=True)
    
    class Meta:
        model = UserDetails
        fields = ['id', 'user', 'user_email', 'user_username', 'profile_image', 
                  'profile_image_url', 'phone_number', 'bio', 'designation', 
                  'organization', 'slug']
        read_only_fields = ['id', 'user', 'slug']
    
    def get_profile_image_url(self, obj):
        return obj.get_image_url
