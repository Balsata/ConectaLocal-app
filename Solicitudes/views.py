from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Solicitudes.forms import SolicitudForm


@login_required(login_url='index')
def crear_solicitud(request):
    form = SolicitudForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../Solicitudes/Solicitud_Creada')

    return render(request, 'Solicitudes/crearSolicitud.html', {'form': form})


@login_required(login_url='index')
def responder_solicitud(request):
    return render(request, 'Solicitudes/responderSolicitud.html', {})


@login_required(login_url='index')
def lista_solicitud(request):
    return render(request, 'Solicitudes/listaSolicitudes.html', {})


@login_required(login_url='index')
def solicitud_Creada(request):
    return render(request, 'Solicitudes/solicitudCreada.html', {})
