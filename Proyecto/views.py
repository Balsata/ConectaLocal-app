from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def index(request):
    return render(request, 'index.html', {})


def password(request):
    return render(request, 'password.html', {})


def inicio(request):
    return render(request, 'inicio.html', {})


class RegistroView(FormView):
    template_name = 'registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
