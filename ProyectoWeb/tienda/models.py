from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    precio=models.FloatField()
    disponible=models.BooleanField(default=True)

    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
