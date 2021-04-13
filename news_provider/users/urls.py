from django.urls import path
from django.contrib.auth.models import User
from .views import login, sign_up


urlpatterns = [
    path('login/', login),
    path('sign-up/', sign_up)
]
