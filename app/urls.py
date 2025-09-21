from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('post', views.create_post, name='create_post'),
    path('post/<int:pk>/delete', views.delete_post, name='delete_post'),
    path('user/<int:pk>/ban', views.ban_user, name='ban_user'),
    path('user/<int:pk>/unban', views.unban_user, name='unban_user'),
]
