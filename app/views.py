from django.shortcuts import render, redirect
from django.contrib.auth import login, logout


def home(request):
    return render(request,'home.html')

