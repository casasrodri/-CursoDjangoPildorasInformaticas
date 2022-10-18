
from django.http import HttpResponse

# Primera vista
def saludo(request):

    documento = '''
        <html>
        <body>
        <h3>
        Hola alumnos, esta es nuestra primera página en Django.
        </h3>
        </body>
        </html>
    '''
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse('Adiós. Vuelva prontos 😀')

# Para uso de contenido dinámico

import datetime
def devuelve_fecha(request):
    now = datetime.datetime.now()

    documento = f'''
        <html>
        <body>
        <h3>
        Fecha y hora actual: {now}
        </h3>
        </body>
        </html>
    '''
    return HttpResponse(documento)

# Paso de parámetros via URL

def edad_futura(request, anio):
    edad = 30
    periodo = anio - 2022
    futuro = edad + periodo

    documento = f'''
        <html>
        <body>
        <h3>
        En el año {anio} tendrás {futuro} años.
        </h3>
        </body>
        </html>
    '''
    return HttpResponse(documento)

def edad_futura_2_param(request, anio, edad):
    #edad = 30
    periodo = anio - 2022
    futuro = edad + periodo

    documento = f'''
        <html>
        <body>
        <h3>
        En el año {anio} tendrás {futuro} años.
        </h3>
        </body>
        </html>
    '''
    return HttpResponse(documento)

# Uso de TEMPLATES

from django.template import Template, Context
class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

def doc_externo(request):
    file = open(r'./Proyecto1/templates/plantilla1.html', 'r')

    template = Template(file.read())
    file.close()

    # Creación del contexto
    nombre = 'Rodri'
    p1 = Persona('Paula', 'Griffa')
    arr = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']

    ctx = Context({
        'nombre_persona': nombre,
        'persona': p1,
        'semestre': arr,
        'now': datetime.datetime.now(),
        'now_formateado': datetime.datetime.now().strftime('%F'),
        'dias': [0, '2323', 'Luquita']
    })

    documento = template.render(ctx)

    return HttpResponse(documento)

from django.template.loader import get_template
def cargador_plantilla(request):

    template = get_template('plantilla1.html')

    # Creación del contexto
    nombre = 'Rodri'
    p1 = Persona('Paula', 'Griffa')
    arr = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']

    # Al usar loaders, no se le pasa un Context(), sino hay que pasarle un diccionario.
    ctx = {
        'nombre_persona': nombre,
        'persona': p1,
        'semestre': arr,
        'now': datetime.datetime.now(),
        'now_formateado': datetime.datetime.now().strftime('%F'),
        'dias': [0, '2323', 'Luquita']
    }

    documento = template.render(ctx)

    return HttpResponse(documento)

# Uso de shorcuts

from django.shortcuts import render
def render_shortcut(request):

    # Creación del contexto
    nombre = 'Rodri'
    p1 = Persona('Paula', 'Griffa')
    arr = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']

    # Al usar loaders, no se le pasa un Context(), sino hay que pasarle un diccionario.
    ctx = {
        'nombre_persona': nombre,
        'persona': p1,
        'semestre': arr,
        'now': datetime.datetime.now(),
        'now_formateado': datetime.datetime.now().strftime('%F'),
        'dias': [0, '2323', 'Luquita']
    }

    return render(request, 'plantilla1.html', ctx)

# Templates incrustados
def uso_menu(request):
    return render(request, 'uso_barra.html')


# Herencia de templates
def template_heredado_ruby(request):
    return render(request, 'curso_ruby.html', {'dameFecha': datetime.datetime.now()})

def template_heredado_css(request):
    return render(request, 'curso_css.html', {'dameFecha': datetime.datetime.now()})
