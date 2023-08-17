from django import forms
from .models import ListaOpen311


class SolicitudFilterForm(forms.Form):
    fecha = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"})
    )

    imagen = forms.ChoiceField(
        required=False,
        choices=[("", "---------"), (True, "Sí"), (False, "No")],
        widget=forms.Select(
            attrs={"class": "form-select select-control", "id": "imagen"})
    )

    descripcion = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "descripcion"})
    )

    direccion = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "direccion"})
    )
