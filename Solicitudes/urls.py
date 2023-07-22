from django.urls import path
from . import views

app_name = 'Solicitudes'

urlpatterns = [
    path('Crear_Solicitud/', views.crear_solicitud, name="crear_solicitud"),
    path('Responder_Solicitud/', views.responder_solicitud, name="responder_solicitud"),
    path('Lista_Solicitudes/', views.lista_solicitud, name="lista_solicitudes"),
]
