## Creación de la estructura del proyecto

- Crear la carpeta `Proyecto`
- Abrir VSCode en esa carpeta

## Crear el entorno virtual

```bash
python -m venv .venv
```

- Activar el entorno desde VSCode como se indica en las diapositivas.

## Crear la estructura del proyecto

- Crear la carpeta `project` (mkdir project)
- Crear el archivo `.gitignore`
- Crear el archivo `README.md`

## Instalación de Django

```bash
pip install django
```

## Crear el proyecto Django y ejecutar el servidor Django

```bash
cd project
django-admin startproject config .
python manage.py runserver
```

- Abrir el navegador y ejecutar el servidor Django en la dirección `127.0.0.1:8000`

## Inicialización de Git

Posicionarse el la raiz del proyecto:

```bash
git init
```

Nota: Git puede pedirte tu configuración (nombre y email) si aún no lo has hecho.

## Primer commit y nueva rama de desarrollo

```bash
git add .
git commit -m "Primer commit"
```

## Comandos para Git

Para mostrar las ramas:
```bash
git branch
```
## Funcionalidad de Clase clientes:
 
- Define los campos "nombre", "apellido", "nacimiento" y "pais_origen_id" para cada cliente


## Funcionalidad de Clase Pais: 

- Define el campo "nombre" para cada país

## Funcionalidad de Clase compra: 

- Define los campos "nombre_compra" y "precio" para el registro de cada compra

## Funcionalidad de la app producto:

-contiene los productos y sus categorías junto con sus CRUD para modificarlas(solo si estas logueado)