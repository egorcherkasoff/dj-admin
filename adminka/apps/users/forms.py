from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, EmailInput


class AuthForm(AuthenticationForm):
    username = forms.EmailField(widget=EmailInput(attrs={"type":"email", "class":"form-control"}))
    password = forms.CharField(widget=PasswordInput(attrs={"type":"password", "class":"form-control mb-3"}))