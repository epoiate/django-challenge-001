from rest_framework import serializers
from .models import Author, Article


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author"""

    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for Article"""

    class Meta:
        model = Article
        fields = '__all__'
