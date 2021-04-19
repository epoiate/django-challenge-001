from django.contrib.auth import login
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, SignUpSerializer
from news.models import Author


# Create your views here.


class LoginAPIView(APIView):
    """
    Login view
    CAUTION: Deprecated!
    """
    # authentication_classes = [To]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Processes authentication"""
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            data = {
                'id': user.pk,
                'token': token.key
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class SignUpAPIView(APIView):
    """Sign-up View"""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Author.objects.get_or_create(id=user, name=user.username)
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            data = {'token': token.key}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
