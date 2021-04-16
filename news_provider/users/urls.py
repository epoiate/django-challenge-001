from django.urls import path

from .views import LoginAPIView, SignUpAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('sign-up/', SignUpAPIView.as_view())
]
