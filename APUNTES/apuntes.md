# Curso Django

## Link del curso

[Lista de reproducción en YouTube](https://www.youtube.com/playlist?list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB)

## Clase 01

### MVC > MTV

Se cambia de Modelo-Vista-Controlador a un **Model-Template-View**, siendo:

* Model > Model
* View > Template
* Controller > View

## Clase 02

Las ventajas de instalar en un entorno virtual, serían las siguientes:

1. Varias versiones de Django/Python
2. Diferentes dependencias para cada proyecto
3. Igualar entornos de dev-test-prod

Bases de datos soportadas oficialmente:

* SQLite3
* PostgreSQL
* MySQL
* Oracle

## Creación de un proyecto

Primero se crea el proyecto:
   `django-admin startproject Proyecto1`

Luego se puede pedir ayuda usando el comando:
`py manage.py help`

Dentro de la carpeta del proyecto, puede verse:

* **__**_init_**__.py**: para que funcione como un paquete.
* **settings.py**: configuración del proyecto, como bases de datos.
* **urls.py**: donde se almacenan las rutas, como un índice.
* **wsgi.py**: relativo al servidor web.

Para crear la base de datos del proyecto (usando **sqlite3**), se debe usar el siguiente comando:
`py manage.py migrate`

Para ejecutar el servidor sencillo, se debe ejecutar:
`py manage.py runserver`

## Clase 03

Para crear las vistas, se debe primero crear un archivo de python para alojarlas, por lo que se crea en la raíz un archivo llamado `views.py`.

## Clase 05

Para utilizar las plantillas, deben seguirse los siguientes pasos:

1. Creación del objeto _Template_.
2. Creación del objeto _Context_.
3. Renderizado del template usando el context.

## Clase 07

Orden en que se evalúa un _punto_ en un template:

1. Diccionario
2. Atributo
3. Método
4. Índice de lista

Igualmente, no se recomienda abusar de estructuras de control de flujo para delegar esa parte a las vistas.

[Información sobre Templates](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/)

## Clase 08

Para usar el cargador de templates _loader_ se debe especificar en el archivo `settings.py` donde se almacenan todas las plantillas.

Buscar la constante `TEMPLATES` y dentro de ese, buscar el array `DIRS`.

## Clase 09

[Shorcuts](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/)

Método `render()`

## Clase 10

### Herencia de templates

Se usa la etiqueta `{% extends 'padre.html' %}`

## Clase 11

Proyecto es _diferente_ a Aplicación.

Un mismo proyecto (por ejemplo tienda online), puede tener varias aplicaciones, como por ejemplo: gestión de stock, gestión de pagos, gestión de envios, promociones.

Luego las aplicaciones pueden usarse en otros proyectos.

### Tablas en Django

Para crear las tablas, se usa la clase Model para que todas hereden de ahí.

Django no puede trabajar con Modelos si no se han creado aplicaciones.

Luego de crear un nuevo proyecto, se deberá inicializar una nueva aplicación, usando: `py manage.py startapp gestionPedidos`

A continuación, se crean en los modelos las distintas clases para que luego impacten en la base de datos.

Después, se registran dichos modelos en la aplicación, en `settings.py`.

Se chequea que todo bien usando el comando: `py manage.py check gestionPedidos`.

Para crear la base de datos, se hace:
`py manage.py makemigrations`

Para que dichas migraciones impacten, se debe hacer en 2 partes:

1. Se genere el código SQL correspondiente, haciendo: `py manage.py sqlmigrate gestionPedidos 0001`.
2. Utilizar dicho código SQL para hacer cambios en la base de datos, haciendo:
`py manage.py migrate`.

## Clase 13

Para hacer un CRUD, se debe ingresar a la consola:
`py manage.py shell` y luego importar el modelo: `from gestionPedidos.models import Articulos`

### Insertar datos

```python
art = Articulos(nombre='mesa', categoria='decoracion', precio=90)

art.save()
```

Otra forma:

```python
Articulos.objects.create(nombre='set de cubiertos', categoria='bazar', precio=120)
```

### Modificar datos

```python
art.precio = 1000
art.save()
```

O buscando el artículo:

```python
art2 = Articulos.object.get(id=2)
art2.nombre= 'set de cubiertos metálicos'
art.save()
```

### Eliminar datos

```python
art3 = Articulos.object.get(id=3)
art.delete()
```

### Consultar datos

Todos los datos:

```python
lista_articulos = Articulos.objects.all()

# Para consultar la query
lista_articulos.query.__str__()
```

Usando tipo _where_:

```python
# Una condición
lista_articulos = Articulos.objects.filter(categoria='bazar')

# Dos condiciones (AND)
lista_articulos = Articulos.objects.filter(categoria='bazar', nombre='tenedor')

# Operadores de comparación
lista_articulos = Articulos.objects.filter(precio__gte=100)

'''
Puede usarse:
 gte -> greater or equal
 gt -> greater
 lte -> less or equal
 lt -> less

'''
```

## Clase 14

Conectando Django con PostgreSQL.

Se debe instalar la libreria _psycopg2_ usando el siguiente comando: `pip install psycopg2`

Luego, en TiendaOnline/settings.py se debe cambiar esta configuración:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

por la siguiente:

```python
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     'TiendaOnlineDjango',
        'USER':     'postgres',
        'PASSWORD': 'root',
        'HOST':     'localhost',
        'PORT':     '5432',
    }
}
```

## Clase 15

### Ordenar los QuerySets

```python
# Orden ascendente
lista_articulos = Articulos.objects.filter(precio__gte=16).order_by('precio')

# Orden descendente
lista_articulos = Articulos.objects.filter(precio__gte=16).order_by('-precio')
```

## Clase 16

### Panel de administración

Debe crearse un super-usuario, dado que no viene por defecto.

```bash
py manage.py createsuperuser
```

En mi caso es `rodri` y el password `1234`.

## Clase 17

Para registrar un modelo en el panel de administrador, debería agregarse lo siguiente en el archivo `gestionPedidos/admin.py`:

```python
from gestionPedidos.models import Clientes
admin.site.register(Clientes)
```

Para hacer que un campo no sea requerido obligatoriamente, es decir, que sea opcional (se denota sin negrita en el panel de admin), se debe cambiar en el modelo, el argumento del campo, especificando `blank=True, null=True`. Y luego hacer todas las migraciones.

## Clase 18

**Cambiar los nombre de los campos en el panel de administración:**
En `models.py` hay que agregar el kwarg `verbose_name=` al constructor de cada campo.
O se puede agregar como primer parámetro, pero no es recomendable porque genera conflictos cuando son campos que se usan como clave foránea o se usan para relación de muchos a muchos.

Si queremos ver más campos en la tabla del panel de administración, se deberá agregar en el archivo `admin.py`, una clase nueva que herede `admin.ModelAdmin`.

Ejemplo:

```python
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre', 'direccion', 'telefono')

# Y luego se registra junto a la clase del modelo
admin.site.register(Clientes, ClienteAdmin)
```

Si queremos tener un buscador, se deberá agregar en el archivo `admin.py`, en la clase que hereda `admin.ModelAdmin`, lo siguiente:

```python
    ...
    search_fields=('nombre','telefono')
```

## Clase 19

Si queremos tener un filtro, se deberá agregar en el archivo `admin.py`, en la clase que hereda `admin.ModelAdmin`, lo siguiente:

```python
class ArticuloAdmin(admin.ModelAdmin):
    list_filter=('seccion')
```

Si es un campo fecha, se puede agregar como un timeline. Usando la siguiente variable:

```python
class PedidoAdmin(admin.ModelAdmin):
    date_hierarchy='fecha'
```

QUEDO EN [ESTE PUNTO](https://youtu.be/DVOAjMuM4vM?t=650)
