from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from .forms import editarPerfil


def index(request):
    return render(request, 'index.html', {})


def password(request):
    return render(request, 'password.html', {})


@login_required(login_url='index')
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
            messages.success(request, success_message)
            return redirect('index')
    return render(request, 'registro.html', {'error_message': error_message, 'username': username})


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(
                request, 'Nombre de usuario o contraseña incorrectos.')
            return redirect('index')
    else:
        if request.user.is_authenticated:
            return redirect('inicio')
        else:
            return render(request, 'index.html')


def logoutCustom(request):
    logout(request)
    return redirect('index')


@login_required(login_url='index')
def perfil(request):
    if request.method == 'POST':
        form = editarPerfil(request.POST, instance=request.user)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            # Validar si el username o email ya existen
            if User.objects.exclude(pk=request.user.pk).filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso.')
            elif User.objects.exclude(pk=request.user.pk).filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya está en uso.')
            else:
                form.save()
                messages.success(request, 'Tus datos se han actualizado correctamente.')
                return redirect('perfil')
    else:
        form = editarPerfil(instance=request.user)
    
    return render(request, 'perfil.html', {'form': form})
