from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class":"form-control mb-3",
            "placeholder":"username",
        })
    )

    password1 = forms.CharField(
        label= 'Password',
        widget=forms.PasswordInput(attrs={
            "class":"form-control mb-3",
            "placeholder":"Password",
        })
    )

    password2 = forms.CharField(
        label= 'Confirm Password',
        widget=forms.PasswordInput(attrs={
            "class":"form-control mb-3",
            "placeholder":"Confirm Password",
        })
    )
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class":"form-control mb-3",
            "placeholder":"username",
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"form-control mb-3",
            "placeholder":"Password",
        })
    )


