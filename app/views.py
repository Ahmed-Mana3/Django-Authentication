from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    pass

def create_post(request):
    return render(request,'post.html')