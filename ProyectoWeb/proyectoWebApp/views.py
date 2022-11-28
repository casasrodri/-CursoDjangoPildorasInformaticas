from django.shortcuts import HttpResponse, render
from carrito.carrito import Carrito

# Create your views here.
def home(request):
    carrito = Carrito(request)
    return render(request, 'proyectoWebApp/home.html')
