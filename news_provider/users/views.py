from django.contrib.auth import login
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer


# Create your views here.


class LoginAPIView(APIView):
    """Login view"""
    # authentication_classes = [To]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Processes authentication"""
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            data = {
                'id': user.pk,
                'token': token.key
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


def sign_up(request):
    """Sign-up new User"""
    # TODO sign-up view
    return HttpResponse("Sign-up view.")
