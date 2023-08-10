from django.db import models


class Solicitud(models.Model):
    fecha_creacion = models.DateTimeField(auto_now=True)
    resuelto = models.BooleanField(default=False)
    nombre = models.CharField(max_length=100)
    tipo_problema = models.CharField(max_length=100)
    tipo_otro = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=20)
    municipio = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    num_ext = models.IntegerField(null=True, blank=True)
    num_int = models.IntegerField(null=True, blank=True)
    codigo_postal = models.IntegerField()
    telefono = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    descripcion = models.CharField(max_length=500)
    archivos = models.FileField(
        upload_to='archivos/', max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.nombre)
