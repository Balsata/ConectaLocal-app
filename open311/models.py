from django.db import models


class ListaOpen311(models.Model):
    descripcion = models.CharField(max_length=600)
    request_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lat = models.IntegerField()
    long = models.IntegerField()
    requested_datetime = models.DateTimeField()
    status = models.CharField(max_length=10)
    media_url = models.CharField(max_length=500, null=True, blank=True)
    agency_responsible = models.CharField(max_length=100, null=True, blank=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.request_id)