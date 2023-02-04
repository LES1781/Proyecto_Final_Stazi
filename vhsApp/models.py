from django.db import models
from django.contrib.auth.models import User


class Cassette(models.Model):

    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    año = models.IntegerField(default=0)
    descripcion = models.TextField(max_length=500)

    def __str__(self):

        return f"cassette: {self.nombre} - Genero: {self.genero}"


class Membresia(models.Model):

    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    facturacion = models.CharField(max_length=20)

    def __str__(self):
        
        return f"Membresia: {self.nombre} - Precio: {self.precio}"


class Solicitar(models.Model):

    solicitud = models.CharField(max_length=500)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):

        return f"Solicitud: {self.solicitud} - Publicado: {self.fecha}"


class Avatar(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user}"
