from django.contrib import admin
from .models import Pedido, ItemPedido
# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ['usuario']

class ItemPedidoAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ['cantidad', 'producto_id']

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)
