from django.shortcuts import render
from rest_framework import viewsets
from .models import Author, Article
from .serializers import AuthorSerializer, ArticleSerializer


# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for Authors"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """ViewSet for Article"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
