from django.contrib import admin
from django.contrib.auth import get_user_model


# Register your models here.

@admin.register(get_user_model())
class Users(admin.ModelAdmin):
    """Admin for CustomUser"""
