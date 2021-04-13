from django.contrib import admin
from .models import Author, Article

# Register your models here.


@admin.register(Author)
class Authors(admin.ModelAdmin):
    """Admin class for Authors"""


@admin.register(Article)
class Articles(admin.ModelAdmin):
    """Admin class for Articles"""
