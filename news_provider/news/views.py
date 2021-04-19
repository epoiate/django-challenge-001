from rest_framework import viewsets, permissions
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from .models import Author, Article
from .serializers import AuthorSerializer, ArticleSerializer, AnonymousArticleSerializer


# Create your views here.


class AdminAuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for Authors"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAdminUser]


class ArticleViewSet(viewsets.GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """ViewSet that implements desired behaviours for Article"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_serializer_class(self):
        """
        Changes what serializer to use according to authentication.
        Authentication requires a header as follows:

        Key:            Value:
        Authentication  Token dd55c313547929bcb7a347c8c3c9394fe4970d08

        The Token can be obtained by using the login view: '/api/login/'
        """
        user = self.request.user
        if user.is_authenticated:
            return ArticleSerializer
        return AnonymousArticleSerializer

    def get_queryset(self):
        """
        Filters queryset by parameters.
        Accepts optional field lookups.
        Ex:
            /api/articles/?category__iexact=:slug
            /api/articles/?summary=:slug&title__icontains=:slug
        """
        queryset = super().get_queryset()
        params = self.request.query_params
        if isinstance(params, dict):
            field_lookups = {}
            for key, value in params.items():
                field_lookups[key] = value
            queryset = queryset.filter(**field_lookups)
        return queryset


class AdminArticleViewSet(viewsets.ModelViewSet):
    """Admin ViewSet for Article"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser]
