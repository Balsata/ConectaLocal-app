from django.urls import path
from . import views

app_name = 'Solicitudes'

urlpatterns = [
    path('Crear_Solicitud/', views.crear_solicitud, name="crear_solicitud"),
]
