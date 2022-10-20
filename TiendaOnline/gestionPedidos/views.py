import re
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.style import context
from gestionPedidos.models import Articulos

# Create your views here.

def search_product(request):
    return render(request, 'busqueda_articulos.html')

def search(request):

    producto = request.GET['prd']

    # Validación de longitud (para evitar sobrecargas del sistema)
    if len(producto) > 20:
        return HttpResponse('<h1 style="color: red">El texto buscado es demasiado largo. Intente nuevamente ☹</h1>')

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

def contacto(request):
    if request.method == 'POST':

        from django.core.mail import send_mail
        from django.conf import settings

        send_mail(
            subject= request.POST['asunto'],
            message= request.POST['mensaje'] + ' ' + request.POST['email'],
            from_email= settings.EMAIL_HOST_USER,
            recipient_list= ['cr.rodrigocasas@gmail.com'],
            fail_silently=False,
        )

        return HttpResponse('Gracias, hemos recibido su mensaje.')
    return render(request, 'contacto.html')
