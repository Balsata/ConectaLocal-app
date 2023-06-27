from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class editarPerfil(UserChangeForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']