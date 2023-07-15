from django.shortcuts import render


def crear_solicitud(request):
    return render(request, 'Solicitudes/crearSolicitud.html', {})
