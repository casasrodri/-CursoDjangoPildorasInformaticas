"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Proyecto1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo', saludo),
    path('adios/', despedida),
    path('datetime', devuelve_fecha),

    # Uso de parámetros en URL
    path('edad/<int:anio>', edad_futura),
    path('edad/<int:edad>/<int:anio>', edad_futura_2_param),

    # Renderizando templates
    path('renderizado1', doc_externo),
    path('renderizado2', cargador_plantilla),
    path('shortcut', render_shortcut),

    # Templates incrustados
    path('uso_menu', uso_menu),

    # Templates heredados
    path('curso_ruby', template_heredado_ruby),
    path('curso_css', template_heredado_css),

]
