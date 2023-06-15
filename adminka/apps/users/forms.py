from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, EmailInput, TextInput, FileInput
from .models import User


class AuthForm(AuthenticationForm):
    username = forms.EmailField(
        widget=EmailInput(attrs={"type": "email", "class": "form-control"})
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={"type": "password", "class": "form-control mb-3"})
    )


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        widget=TextInput(attrs={"type": "text", "class": "form-control"}),
    )
    middle_name = forms.CharField(
        max_length=100,
        widget=TextInput(attrs={"type": "text", "class": "form-control"}),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=TextInput(attrs={"type": "text", "class": "form-control"}),
    )
    email = forms.EmailField(
        max_length=100,
        widget=TextInput(attrs={"type": "email", "class": "form-control"}),
    )
    avatar = forms.ImageField(
        required=False,
        widget=FileInput(attrs={"type": "file", "class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ["first_name", "middle_name", "last_name", "email", "avatar"]


class UserCreateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        widget=TextInput(attrs={"type": "text", "class": "form-control"}),
    )
    middle_name = forms.CharField(
        max_length=100,
        widget=TextInput(attrs={"type": "text", "class": "form-control"}),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=TextInput(attrs={"type": "text", "class": "form-control"}),
    )
    email = forms.EmailField(
        max_length=100,
        widget=TextInput(attrs={"type": "email", "class": "form-control"}),
    )
    password = forms.CharField(
        max_length=50,
        widget=PasswordInput(attrs={"type": "password", "class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ["first_name", "middle_name", "last_name", "email", "password"]
