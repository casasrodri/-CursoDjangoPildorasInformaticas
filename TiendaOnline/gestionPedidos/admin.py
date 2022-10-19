from django.contrib import admin

# Register your models here.

from gestionPedidos.models import Clientes
admin.site.register(Clientes)

from gestionPedidos.models import Articulos
admin.site.register(Articulos)

from gestionPedidos.models import Pedidos
admin.site.register(Pedidos)
