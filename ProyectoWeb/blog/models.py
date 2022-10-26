from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)

    # Relación de uno a uno
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # Relación many-to-many
    categorias = models.ManyToManyField(Categoria)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self) -> str:
        return self.titulo
