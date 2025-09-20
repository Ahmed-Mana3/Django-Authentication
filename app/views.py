from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html', {'posts':posts})

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(
            title = title,
            content = content,
            username = request.user
        )
        return redirect("home")
    return render(request, 'post.html')

