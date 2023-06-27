from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import registro
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('registro/', registro, name="registro"),
    path('password/', views.password, name="password"),
    path('logout', views.logoutCustom, name='logout'),
    path('inicio/', views.inicio, name="inicio"),
    path('perfil/', views.perfil, name='perfil'),
    path('Solicitudes/', include('Solicitudes.urls')),
    path('admin/', admin.site.urls)
]
