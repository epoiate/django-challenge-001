from django.urls import path, include
from rest_framework import routers

from .views import AdminAuthorViewSet, AdminArticleViewSet, ArticleViewSet

admin_router = routers.DefaultRouter()
admin_router.register('articles', AdminArticleViewSet, basename='admin_rticles')
admin_router.register('authors', AdminAuthorViewSet, basename='admin_authors')

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, basename='Articles')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', include(admin_router.urls)),
]
