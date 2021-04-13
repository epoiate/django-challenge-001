from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def login(request):
    """Login User"""
    # TODO login view
    return HttpResponse("Login view.")


def sign_up(request):
    """Sign-up new User"""
    # TODO sign-up view
    return HttpResponse("Sign-up view.")
