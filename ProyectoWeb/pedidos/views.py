from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido, ItemPedido
from carrito.carrito import Carrito
from tienda.models import Producto
from django.contrib import messages

# Create your views here.

@login_required(login_url='/autenticacion/loguear')
def procesar_pedido(request):
    pedido = Pedido.objects.create(usuario=request.user)
    carrito = Carrito(request)

    lineas_pedido = list()

    for k,v in carrito.carrito.items():
        lineas_pedido.append(
            ItemPedido(
                producto_id = Producto.objects.get(id=k),
                cantidad = v['cantidad'],
                pedido_id = pedido
            )
        )

    ItemPedido.objects.bulk_create(lineas_pedido)

    enviar_email(
        pedido=pedido,
        lineas_pedido= lineas_pedido,
        usuario = request.user.username,
        email = request.user.email
    )

    messages.success(request, "El pedido se ha creado correctamente.")

    carrito.vaciar()

    return redirect('tienda')

def enviar_email(pedido, lineas_pedido, usuario, email):
    print(pedido, lineas_pedido, usuario, email)
    return None
