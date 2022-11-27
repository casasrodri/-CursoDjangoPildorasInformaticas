# Proyecto completo usando Django

## Clase 27

El menú tendrá: Home, Servicios, Tienda, Blog, Contacto y (admin)

Elemento | Nombre
-|-
Proyecto | ProyectoWeb
App | proyectoWebApp

Para hacerlo, ejecuté las siguientes instrucciones:

```bash
django-admin startproject ProyectoWeb
cd .\ProyectoWeb\
py manage.py startapp proyectoWebApp
```

## Clase 29

Uso de Bootstrap

Descargamos el zip y lo guardamos en `proyectoWebApp/static/proyectoWebApp` a las carpetas `css`, `img` y `vendor`.

## Clase 30

Ver las opciones adicionales para los modelos, usando la clase Meta.

## Clase 34

Al subir imagenes, django no está preparado para mostrárnolas por defecto en el modo dev, y además se suben en la raíz, asi que hay que hacer lo siguiente para corregir esto.

### Ordenar

Se crea una carpeta `media` al mismo nivel de las apps.

### Indicar que ahi está la info

En el archivo `settings.py` se debe crear la siguiente configuración:

```python
MEDIA_URL = '/media'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Luego se debe agregar en el `urls.py` el siguiente código:

```python
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Me quedé en: [video 65](https://www.youtube.com/watch?v=zd9Ipe0BTpQ&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB&index=65)
