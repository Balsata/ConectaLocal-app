from django.shortcuts import render


def crear_solicitud(request):
    return render(request, 'Solicitudes/crearSolicitud.html', {})

def responder_solicitud(request):
    return render(request, 'Solicitudes/responderSolicitud.html', {})

def lista_solicitud(request):
    return render(request, 'Solicitudes/listaSolicitudes.html', {})
