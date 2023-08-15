from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Solicitudes.forms import SolicitudForm, SolicitudFilterForm, RespuestaForm
from Solicitudes.models import Solicitud
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.utils.dateparse import parse_date


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
    form = SolicitudFilterForm(request.GET)
    solicitudes = Solicitud.objects.all()

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        estado = form.cleaned_data.get('estado')
        municipio = form.cleaned_data.get('municipio')
        tipo_problema = form.cleaned_data.get('tipo_problema')
        resuelto = form.cleaned_data.get('resuelto')
        fecha = form.cleaned_data.get('fecha')

        if nombre:
            solicitudes = solicitudes.filter(nombre__icontains=nombre)
        if estado:
            solicitudes = solicitudes.filter(estado__icontains=estado)
        if municipio:
            solicitudes = solicitudes.filter(municipio__icontains=municipio)
        if resuelto is not None and resuelto != "":
            solicitudes = solicitudes.filter(resuelto=resuelto)
        if tipo_problema:
            solicitudes = solicitudes.filter(
                tipo_problema__icontains=tipo_problema)
        if fecha:
            fecha_parsed = parse_date(str(fecha))
            if fecha_parsed:
                solicitudes = solicitudes.filter(
                    fecha_creacion__date=fecha_parsed)
        if not solicitudes.exists():
            messages.info(
                request, 'No se encontraron resultados con los filtros seleccionados.')

    if request.method == 'POST':
        action = request.POST.get('action')

        if action:
            if action.startswith('eliminar_'):
                solicitud_id = action.replace('eliminar_', '')
                solicitud = get_object_or_404(Solicitud, id=solicitud_id)
                solicitud.delete()
                messages.success(request, 'La solicitud ha sido eliminada.')

                return redirect('Solicitudes:responder_solicitud')

    return render(request, 'Solicitudes/responderSolicitud.html', {'solicitudes': solicitudes, 'form': form})


@login_required(login_url='index')
def lista_solicitud(request):
    form = SolicitudFilterForm(request.GET)
    solicitudes = Solicitud.objects.all()

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        estado = form.cleaned_data.get('estado')
        municipio = form.cleaned_data.get('municipio')
        tipo_problema = form.cleaned_data.get('tipo_problema')
        resuelto = form.cleaned_data.get('resuelto')
        fecha = form.cleaned_data.get('fecha')

        if nombre:
            solicitudes = solicitudes.filter(nombre__icontains=nombre)
        if estado:
            solicitudes = solicitudes.filter(estado__icontains=estado)
        if municipio:
            solicitudes = solicitudes.filter(municipio__icontains=municipio)
        if resuelto is not None and resuelto != "":
            solicitudes = solicitudes.filter(resuelto=resuelto)
        if tipo_problema:
            solicitudes = solicitudes.filter(
                tipo_problema__icontains=tipo_problema)
        if fecha:
            fecha_parsed = parse_date(str(fecha))
            if fecha_parsed:
                solicitudes = solicitudes.filter(
                    fecha_creacion__date=fecha_parsed)
        if not solicitudes.exists():
            messages.info(
                request, 'No se encontraron resultados con los filtros seleccionados.')

    return render(request, 'Solicitudes/listaSolicitudes.html', {'solicitudes': solicitudes, 'form': form})


@login_required(login_url='index')
def solicitud_Creada(request):
    return render(request, 'Solicitudes/solicitudCreada.html', {})


@login_required(login_url='index')
def detalles_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    return render(request, 'Solicitudes/detalles_solicitud.html', {'solicitud': solicitud})


@login_required(login_url='index')
def editar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)

    if request.method == 'POST':
        form = SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            messages.success(request, 'La solicitud ha sido actualizada.')
            return redirect('Solicitudes:lista_solicitudes')
    else:
        form = SolicitudForm(instance=solicitud)

    return render(request, 'Solicitudes/editar_Solicitud.html', {'form': form, 'solicitud': solicitud})


@login_required(login_url='index')
def respuesta_de_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)

    if request.method == 'POST':
        respuesta_form = RespuestaForm(
            request.POST, request.FILES, instance=solicitud)

        if respuesta_form.is_valid():
            respuesta_form.save()

            # Verificar si los campos de respuesta han sido completados
            if (respuesta_form.cleaned_data['nombre_respuesta'] and
                    respuesta_form.cleaned_data['puesto_respuesta'] and
                    respuesta_form.cleaned_data['detalle_respuesta']):
                solicitud.resuelto = True
                solicitud.save()
            messages.success(request, 'La solicitud ha sido respondida.')
            return redirect('Solicitudes:responder_solicitud')

        else:
            print(respuesta_form.errors)
    else:
        respuesta_form = RespuestaForm(instance=solicitud)

    return render(request, 'Solicitudes/respuesta_de_solicitud.html', {'respuesta_form': respuesta_form, 'solicitud': solicitud})
