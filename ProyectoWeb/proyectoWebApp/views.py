from django.shortcuts import HttpResponse, render


# Create your views here.
def home(request):
    return render(request, 'proyectoWebApp/home.html')

def tienda(request):
    return render(request, 'proyectoWebApp/tienda.html')
