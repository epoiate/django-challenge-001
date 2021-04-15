from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


# Create your serializers here.


class LoginSerializer(serializers.Serializer):
    """Serializer for login process"""

    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=255, style={'input_type': 'password', })

    def validate(self, data: dict) -> dict:
        username = data.get('username', None)
        password = data.get('password', None)
        request = self.context.get('request')

        user = authenticate(request, username=username, password=password)
        if not user:
            raise ValidationError('Authentication failed.', code='authorization')
            return data
        data['user'] = user
        return data
