from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import SignUpAPIView, LoginAPIView

urlpatterns = [
    path('login/', obtain_auth_token),
    path('sign-up/', SignUpAPIView.as_view())
]
