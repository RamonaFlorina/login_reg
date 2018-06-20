from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def success(request):
    return render (request, 'success.html')
