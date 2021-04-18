from django.contrib import admin

from .models import Author, Article


# Register your models here.


@admin.register(Author)
class Authors(admin.ModelAdmin):
    """Admin class for Authors"""

    list_display = ['name', ]
    list_display_links = ['name', ]


@admin.register(Article)
class Articles(admin.ModelAdmin):
    """Admin class for Articles"""

    list_display = ['title', 'author', ]
    list_display_links = ['title', 'author', ]
