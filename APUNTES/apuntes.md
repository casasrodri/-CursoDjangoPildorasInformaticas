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
2. Utilice dicho código SQL para hacer cambios en la base de datos, haciendo:
`py manage.py migrate`.
