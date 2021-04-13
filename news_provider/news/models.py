from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    picture = models.ImageField()


class Article(models.Model):
    """"""

    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    firstParagraph = models.TextField()
    body = models.TextField()
