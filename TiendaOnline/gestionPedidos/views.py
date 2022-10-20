from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.style import context
from gestionPedidos.models import Articulos

# Create your views here.

def search_product(request):
    return render(request, 'busqueda_articulos.html')

def search(request):

    producto = request.GET['prd']
    if producto == '':
        mensaje = 'No se han ingresado términos en la búsqueda.'
    else:
        #mensaje='Articulo buscado: %r' % producto

        encontrados = Articulos.objects.filter(nombre__icontains=producto)

        if encontrados:
            # mensaje = 'Se han encontrado los siguientes artículos:<br>'
            # for e in encontrados:
            #     mensaje = mensaje + f'  > {e}<br>'

            contexto = {
                'articulos': encontrados,
                'buscado': producto
            }

            return render(request, 'resultados_busqueda.html', contexto)
        else:
            mensaje = 'No se han encontrado artículos.'
    print()
    print('---------------------------------------------------')
    #print(request.__dict__)
    print('---------------------------------------------------')
    print()

    return HttpResponse(mensaje)
