from django.urls import path
from . import views

app_name = 'Solicitudes'

urlpatterns = [
    path('Crear_Solicitud/', views.crear_solicitud, name="crear_solicitud"),
    path('Responder_Solicitud/', views.responder_solicitud, name="responder_solicitud"),
    path('Lista_Solicitudes/', views.lista_solicitud, name="lista_solicitudes"),
    path('Solicitud_Creada/', views.solicitud_Creada, name="solicitud_Creada"),
    path('Solicitud/<int:solicitud_id>/', views.detalles_solicitud, name='detalles_solicitud'),
    path('Editar_Solicitud/<int:solicitud_id>/', views.editar_solicitud, name='editar_solicitud'),
    path('Respuesta_de_solicitud/<int:solicitud_id>/', views.respuesta_de_solicitud, name='respuesta_de_solicitud'),
]
