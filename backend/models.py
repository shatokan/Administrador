from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    usuario = models.OneToOneField(User, verbose_name='Usuario', related_name='userapp',on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    rut = models.CharField(max_length=30,unique=True)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    region = models.ForeignKey('Region', blank=True, null=True, on_delete=models.SET_NULL)

class Marca(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

class Estilo(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

class Color(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

class Region(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

class Aro(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

class Bicicleta(models.Model):
    modelo = models.CharField(max_length=255)
    numero_serie = models.CharField(max_length=255)
    descripcion = models.TextField(default='')
    factura = models.ImageField('Factura', upload_to='facturas/',blank=True)
    foto = models.ImageField('Foto', upload_to='fotos/',blank=True)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    estilo = models.ForeignKey('Estilo', on_delete=models.CASCADE)
    aro = models.ForeignKey('Aro', on_delete=models.CASCADE)
    color_primario = models.ForeignKey('Color', related_name='color_primario', on_delete=models.CASCADE)
    color_secundario = models.ForeignKey('Color', related_name='color_secundario', on_delete=models.CASCADE)