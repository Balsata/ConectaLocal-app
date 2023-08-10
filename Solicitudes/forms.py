from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):

    TIPO_PROBLEMA_CHOICES = [
        ("", "-- Selecciona una opción --"),
        ("1", "Otro"),
        ("Aceras o banquetas dañadas", "Aceras o banquetas dañadas"),
        ("Baches en calles y carreteras", "Baches en calles y carreteras"),
        ("Basura acumulada en áreas públicas",
         "Basura acumulada en áreas públicas"),
        ("Contenedores de basura dañados o desbordados",
         "Contenedores de basura dañados o desbordados"),
        ("Daños en infraestructuras deportivas (canchas, pistas, etc.)",
         "Daños en infraestructuras deportivas (canchas, pistas, etc.)"),
        ("Desperdicio de agua en áreas públicas",
         "Desperdicio de agua en áreas públicas"),
        ("Falta de acceso a servicios médicos o de emergencia",
         "Falta de acceso a servicios médicos o de emergencia"),
        ("Falta de iluminación en calles o espacios públicos",
         "Falta de iluminación en calles o espacios públicos"),
        ("Falta de mantenimiento en edificios públicos",
         "Falta de mantenimiento en edificios públicos"),
        ("Falta de mantenimiento en parques y áreas verdes",
         "Falta de mantenimiento en parques y áreas verdes"),
        ("Falta de señalización o semáforos en intersecciones peligrosas",
         "Falta de señalización o semáforos en intersecciones peligrosas"),
        ("Graffiti o pintadas vandálicas", "Graffiti o pintadas vandálicas"),
        ("Infestación de plagas en espacios públicos",
         "Infestación de plagas en espacios públicos"),
        ("Inundaciones o problemas de drenaje en áreas urbanas",
         "Inundaciones o problemas de drenaje en áreas urbanas"),
        ("Mobiliario urbano deteriorado (bancos, señalización, etc.)",
         "Mobiliario urbano deteriorado (bancos, señalización, etc.)"),
        ("Problemas con el suministro de agua potable",
         "Problemas con el suministro de agua potable"),
        ("Problemas con el transporte público (retrasos, falta de unidades, etc.)",
         "Problemas con el transporte público (retrasos, falta de unidades, etc.)"),
        ("Problemas de ruido o contaminación ambiental",
         "Problemas de ruido o contaminación ambiental"),
        ("Problemas de tráfico o congestión vehicular",
         "Problemas de tráfico o congestión vehicular"),
        ("Vías ciclistas en mal estado", "Vías ciclistas en mal estado"),
    ]

    ESTADOS = [


        ("", "-- Selecciona --"),
        ("Aguascalientes", "Aguascalientes"),
        ("Baja California", "Baja California"),
        ("Baja California Sur", "Baja California Sur"),
        ("Campeche", "Campeche"),
        ("Chiapas", "Chiapas"),
        ("Chihuahua", "Chihuahua"),
        ("Ciudad de Mexico", "Ciudad de Mexico"),
        ("Coahuila", "Coahuila"),
        ("Colima", "Colima"),
        ("Durango", "Durango"),
        ("Guerrero", "Guerrrero"),
        ("Guanajuato", "Guanajuato"),
        ("Hidalgo", "Hidalgo"),
        ("Jalisco", "Jalisco"),
        ("Michoacan", "Michoacan"),
        ("Estado de Mexico", "Estado de Mexico"),
        ("Morelos", "Morelos"),
        ("Nayarit", "Nayarit"),
        ("Nuevo Leon", "Nuevo Leon"),
        ("Oaxaca", "Oaxaca"),
        ("Puebla", "Puebla"),
        ("Quintana Roo", "Quintana Roo"),
        ("Queretaro", "Queretaro"),
        ("Sinaloa", "Sinaloa"),
        ("San Luis Potosi", "San Luis Potosi"),
        ("Sonora", "Sonora"),
        ("Tabasco", "Tabasco"),
        ("Tlaxcala", "Tlaxcala"),
        ("Tamaulipas", "Tamaulipas"),
        ("Veracruz", "Veracruz"),
        ("Yucatan", "Yucatan"),
        ("Zacatecas", "Zacatecas"),
    ]

    class Meta:
        model = Solicitud
        fields = ["nombre", "tipo_problema", "tipo_otro", "estado", "municipio", "direccion",
                  "num_ext", "num_int", "codigo_postal", "telefono", "email", "descripcion", "archivos"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Titulo de la solicitud", "requiered": "True"}),
            "tipo_otro": forms.TextInput(attrs={"class": "form-control", "placeholder": "Otro problema" "disable"}),
            "municipio": forms.Select(attrs={"class": "form-select", "id": "municipio", "requiered": "True"}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "id": "direccion", "placeholder": "direccion", "requiered": "True"}),
            "num_ext": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Numero exterior"}),
            "num_int": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Numero interior"}),
            "codigo_postal": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Codgio postal", "requiered": "True"}),
            "telefono": forms.TextInput(attrs={"class": "form-control", "id": "telefono", "placeholder": "telefono", "requiered": "True"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "id": "email-contacto", "placeholder": "email-contacto", "requiered": "True"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descripcion", "id": "descripcion", "style": "height: 300px", "requiered": "True"}),
            "archivos": forms.FileInput(attrs={"class": "form-control", "id": "evidencia"}),
        }

    tipo_problema = forms.ChoiceField(
        choices=TIPO_PROBLEMA_CHOICES,
        widget=forms.Select(
            attrs={"class": "form-select", "aria-label": "Floating label select example", "id": "problem", "onchange": "problema()", "requiered": "True"})
    )

    estado = forms.ChoiceField(
        choices=ESTADOS,
        widget=forms.Select(
            attrs={"class": "form-select", "id": "estado", "onchange": "cargarMunicipios()", "requiered": "True"})
    )
