from django.shortcuts import render, redirect
from .carrito import Carrito
from tienda.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    carrito.agregar(producto)

    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    carrito.eliminar(producto)

    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    carrito.restar_producto(producto)

    return redirect("tienda")

def vaciar(request):
    carrito = Carrito(request)
    carrito.vaciar()

    return redirect("tienda")
