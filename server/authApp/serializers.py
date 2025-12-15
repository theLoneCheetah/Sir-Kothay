from rest_framework import serializers
from .models import CustomUser
from dashboard.models import UserDetails


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password', 'first_name', 'last_name', 'is_active', 'date_joined']
        read_only_fields = ['id', 'date_joined']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(**validated_data, password=password)
        # Create UserDetails for new user
        UserDetails.objects.create(user=user, phone_number='', bio='', designation='', organization='')
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
