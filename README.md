# Proyecto Django de Silabuz Unidad 4

[![N|Solid](https://railway.app/brand/logotype-dark.png)](https://djangoportafolio-production-9df7.up.railway.app)

## Descripcíon
- Es un Proyecto de Django que se encarga de crear un Portafolio
- Para crear un Portafolio el usuario tiene que registre, Despues de que se Registre le mostrara un formulario para la creacion de su proyecto 
de GitHub, le pedira que Inserte el Titulo, Descripcíon, URL y una foto del Proyecto.
- El Usuario solo podra visualizar su Portafolio
- Si no se a registrado, no podra crear su Proyecto le enviara a la pagina de Login
- La pagina Inicial solo es un Ejemplo de su portafolio, pero no sera igual
- La aplicacion Guarda la IP cuando visita la pagina, si no se a registro sale como Anonymous y si se registro sale con el nombre del User
- Para ver la Lista de IP esta en http://127.0.0.1:8000/ip/

## Requisitos
- Python 3.10

## Instalacion
#### Crear entorno Virtual
```bash
python3 -m venv env
```
#### Activar el entorno Virtual (Windows)
```bash
env\Scripts\activate.bat
```
#### Instalar los Requisitos
```bash
pip install -r requirements.txt
```
#### Migrar Base de Datos
La base esta en SQLite
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
#### Iniciar Proyecto
```bash
python manage.py runserver
```

