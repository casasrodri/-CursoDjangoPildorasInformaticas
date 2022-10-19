from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=7, verbose_name='teléfono celular')

    def __str__(self) -> str:
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return f'Artículo [nombre={self.nombre}, categoria={self.categoria}, precio={self.precio}]'

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
