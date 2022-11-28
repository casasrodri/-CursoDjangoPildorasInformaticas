from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido, ItemPedido
from carrito.carrito import Carrito
from tienda.models import Producto
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

@login_required(login_url='/autenticacion/loguear')
def procesar_pedido(request):
    pedido = Pedido.objects.create(usuario=request.user)
    carrito = Carrito(request)

    lineas_pedido = list()

    for k,v in carrito.carrito.items():
        lineas_pedido.append(
            ItemPedido(
                producto = Producto.objects.get(id=k),
                cantidad = v['cantidad'],
                pedido = pedido
            )
        )

    ItemPedido.objects.bulk_create(lineas_pedido)

    enviar_email(
        pedido=pedido,
        lineas_pedido= lineas_pedido,
        usuario = request.user.username,
        email = request.user.email
    )

    carrito.vaciar()

    messages.success(request, "El pedido se ha creado correctamente.")

    return redirect('tienda')

def enviar_email(**kwargs):

    asunto = "Gracias por su pedido!"
    mensaje = render_to_string('emails/pedido.html', {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "usuario": kwargs.get("usuario"),
        "email": kwargs.get("email")
    })

    mensaje_texto = strip_tags(mensaje)

    from_email = "tienda@tienda.com"
    to_email = kwargs.get("email")

    send_mail(
        asunto,
        mensaje_texto,
        from_email,
        [to_email],  # type: ignore
        html_message= mensaje
    )
