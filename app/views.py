from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Post
from users.models import ModUsers, BanedUsers

def home(request):
    posts = Post.objects.all().order_by('-created_at')  
    if request.user.is_authenticated:
        is_mod = ModUsers.objects.filter(user=request.user).exists()
    else:
        is_mod = False
    banned_users = BanedUsers.objects.values_list("user", flat=True)
    return render(request,'home.html', {'posts':posts, 'banned_users':banned_users,'is_mod':is_mod, 'request':request})

@login_required
def create_post(request):
    if not BanedUsers.objects.filter(user=request.user).exists():
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
    return render(request, 'post.html')
    

@login_required
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')


def is_mod(user):
    if ModUsers.objects.filter(user=user).exists():
        return True
    return False 

@login_required
def ban_user(request, pk):
    post = Post.objects.get(pk=pk)
    user = post.username
    BanedUsers.objects.create(user=user)
    return redirect('home')

@login_required
def unban_user(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        user = post.username
        banned_user = BanedUsers.objects.get(user=user)
        banned_user.delete()
        return redirect('home')
    except:
        return redirect('home')


def user_profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(username=user).order_by('-created_at')  
    is_mod = False
    if request.user.is_authenticated:
        is_mod = ModUsers.objects.filter(user=request.user).exists()
    is_owner = False
    if request.user == user and request.user.is_authenticated:
        is_owner = True
    context = {
       'user':user,
       'posts':posts,
       'request':request,
       'is_mod':is_mod,
       'is_owner':is_owner
    }
    return render(request, 'user_profile.html', context)


def user_profile_by_post(request, pk):
    post = Post.objects.get(pk=pk)
    username = post.username
    posts = Post.objects.filter(username=username).order_by('-created_at')  
    user = User.objects.get(username=username)
    is_mod = False
    if request.user.is_authenticated:
        is_mod = ModUsers.objects.filter(user=request.user).exists()    
    context = {
       'user':user,
       'posts':posts,
       'request':request,
       'is_mod':is_mod
    }
    return render(request, 'user_profile.html', context)