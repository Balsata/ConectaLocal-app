from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html', {})


def password(request):
    return render(request, 'password.html', {})


def inicio(request):
    return render(request, 'inicio.html', {})


def registro(request):
    error_message = ''
    success_message = ''
    username = ''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            error_message = 'Nombre de usuario ya existe.'
        elif User.objects.filter(email=email).exists():
            error_message = 'Correo electrónico ya existe.'
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            success_message = 'El usuario se ha registrado exitosamente.'
            return redirect('index')
    return render(request, 'registro.html', {'error_message': error_message, 'username': username, 'success_message': success_message})


def logoutCustom(request):
    logout(request)
    return redirect('index')
