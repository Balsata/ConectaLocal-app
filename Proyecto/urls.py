from django.contrib import admin
from django.urls import path
from .views import RegistroView
from . import views

urlpatterns = [
    path('', views.index , name = "index"),
    path('registro/', RegistroView.as_view(), name = "registro"),
    path('password/', views.password, name = "password"),
    path('admin/', admin.site.urls)
]
