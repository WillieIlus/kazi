from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'role', 'avatar', 'is_staff', 'is_active', 'date_joined', 'last_login')
        read_only_fields = ('id', 'is_staff', 'is_active', 'date_joined', 'last_login')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'is_staff', 'is_active', 'date_joined', 'last_login')


