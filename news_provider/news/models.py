import uuid

from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


class Author(models.Model):
    """
    Author model.
    Assuming not all users are Authors
    """

    id = models.OneToOneField(get_user_model(), primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='images/%Y/%m/%d/', default='images/generic_user.png')

    def __str__(self):
        return self.name


class Article(models.Model):
    """Article model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    firstParagraph = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title
