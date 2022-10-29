from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    formulario = FormularioContacto()

    if request.method == "POST":
        formulario = FormularioContacto(data=request.POST)

        if formulario.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email = EmailMessage(
                subject= "Mensaje de Gestión de Pedidos [Web]",
                body= f"El usuario {nombre} ({email}) escribe lo siguiente:\n\n{contenido}",
                from_email= "",
                to=['cr.rodrigocasas@gmail.com'],
                reply_to=[email]
            )

            try:
                email.send()
                # Al apretar enviar, se recarga la página, entonces podemos redirigirlo a un "OK"
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')

    return render(request, 'contacto/contacto.html', {'miFormulario': formulario})
