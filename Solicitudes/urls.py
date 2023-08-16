from django.urls import path
from . import views
from .views import SolicitudListaView, SolicitudDetalleView, TokenObtainView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Solicitudes API",
        default_version='v1',
        description="API para la vista y creacion de solicitudes",
        terms_of_service="https://www.myapp.com/terms/",
        contact=openapi.Contact(email="bryanalexst@hotmail.com"),
        license=openapi.License(name="Licencia"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'Solicitudes'

urlpatterns = [
    path('Crear_Solicitud/', views.crear_solicitud, name="crear_solicitud"),
    path('Responder_Solicitud/', views.responder_solicitud, name="responder_solicitud"),
    path('Lista_Solicitudes/', views.lista_solicitud, name="lista_solicitudes"),
    path('Solicitud_Creada/', views.solicitud_Creada, name="solicitud_Creada"),
    path('Solicitud/<int:solicitud_id>/', views.detalles_solicitud, name='detalles_solicitud'),
    path('Editar_Solicitud/<int:solicitud_id>/', views.editar_solicitud, name='editar_solicitud'),
    path('Respuesta_de_solicitud/<int:solicitud_id>/', views.respuesta_de_solicitud, name='respuesta_de_solicitud'),
    path('solicitudes/', SolicitudListaView.as_view(), name='solicitud-lista'),
    path('solicitudes/<int:pk>/', SolicitudDetalleView.as_view(), name='solicitud-detalle'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('token/', TokenObtainView.as_view(), name='token_obtain'),
]
