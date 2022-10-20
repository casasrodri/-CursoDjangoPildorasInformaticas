from django.contrib import admin

# Register your models here.

from gestionPedidos.models import Clientes, Articulos, Pedidos

# Para ver más campos en la vista del administrador:

class ClienteAdmin(admin.ModelAdmin):
    list_display=['nombre', 'direccion', 'telefono']
    search_fields=['nombre','direccion']

class ArticuloAdmin(admin.ModelAdmin):
    search_fields= ['nombre']
    list_filter=['categoria']

class PedidoAdmin(admin.ModelAdmin):
    date_hierarchy='fecha'
    list_display=['numero', 'fecha']

# Registramos las clases en el sitio
admin.site.register(Clientes, ClienteAdmin)
admin.site.register(Articulos, ArticuloAdmin)
admin.site.register(Pedidos,PedidoAdmin)
