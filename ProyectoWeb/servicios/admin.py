from django.contrib import admin
from .models import Servicio

# Register your models here.


class ServicioAdimin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['titulo', 'contenido']

admin.site.register(Servicio, ServicioAdimin)
