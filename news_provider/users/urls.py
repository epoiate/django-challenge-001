from django.urls import path

from .views import LoginAPIView, sign_up

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('sign-up/', sign_up)
]
