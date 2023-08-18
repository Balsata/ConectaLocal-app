from django.urls import path 
from . import views

app_name = 'open311'

urlpatterns = [
    path('solicitud', views.solicitud, name='solicitud'),
    path('lista_open311', views.lista_solicitudes, name='lista_open311'),
    path('generar_reporte/', views.generar_reporte, name='generar_reporte'),
]
