from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import CustomUser


# Create your serializers here.


class LoginSerializer(serializers.Serializer):
    """
    Serializer for login process
    CAUTION: Deprecated!
    """

    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=255, style={'input_type': 'password', })

    def validate(self, data: dict) -> dict:
        username = data.get('username', None)
        password = data.get('password', None)
        request = self.context.get('request')

        user = authenticate(request, username=username, password=password)
        if not user:
            raise serializers.ValidationError('Authentication failed.', code='authorization')
            return data
        data['user'] = user
        return data


class SignUpSerializer(serializers.Serializer):
    """Serializer for sign-up process"""

    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=255, style={'input_type': 'password', })
    email = serializers.EmailField(max_length=32)
    confirm_password = serializers.CharField(max_length=255, style={'input_type': 'password', })

    def update(self, instance, validated_data):
        pass

    def validate_username(self, username):
        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'Username already exists', })
        return username

    def validate(self, data: dict) -> dict:
        password = data.get('password', None)
        confirm_password = data.get('confirm_password', None)

        if password != confirm_password and password is not None:
            raise serializers.ValidationError({'confirm_password': 'Passwords did not match.', })

        return data

    def create(self, validated_data):
        username = validated_data.get('username', None)
        email = validated_data.get('email', None)
        password = validated_data.get('password', None)

        return CustomUser.objects.create_user(username=username, password=password, email=email)
