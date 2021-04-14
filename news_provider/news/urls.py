from django.urls import path, include

from rest_framework import routers
from .views import AuthorViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, basename='Articles')
router.register('authors', AuthorViewSet, basename='Authors')

urlpatterns = [
    path('', include(router.urls)),
]
