
# Profiles REST API

Profiles REST API course code

--------------------

## Commands

```sh
    vagrant init ubuntu/bionic64
```

> Inicializa un archivo de configuración Vagrant en el directorio actual y lo configura para utilizar la imagen de la máquina virtual "ubuntu/bionic64".

```sh
    vagrant up
```

> Crear y configurar una máquina virtual utilizando el archivo **Vagrantfile**.

```sh
    vagrant ssh
```

> Inicializa una sesión SSH en una máquina virtual que ha sido creada y configurada con Vagrant.
>
> Después de ejecutar "vagrant ssh", se establecerá una conexión SSH con la máquina virtual en la que se ejecutará el shell de la terminal de la máquina virtual en la consola del host donde se ejecuta Vagrant. Esto permite al usuario interactuar con la máquina virtual como si estuviera trabajando directamente en ella.

```sh
    django-admin.py startproject profiles_projects .
```

> Llama al script del archivo .py, el segundo parametro es para indicarle que queremos crear un nuevo proyecto, luego indicamos el nombre del proyecto y el ultimo comando, en este caso **'.'** es para indicarle el path donde queremos crear el projecto

### Se nos creara el siguiente proyecto

![project init](readme_imgs\django_script_img.png)

```sh
    python manage.py startapp profiles_api
```

> Crea la app para nuestro ***profiles_project***

### Se nos creara el siguiente directorio que contendra la app

![app init](readme_imgs\django_app_script.py.png)

```sh
    python manage.py runserver 0.0.0.0:8000
```

> Ejecutamos el script manage.py y le indicamos que queremos correr el servidor con el comando **runserver**, en este caso, en el puerto 8000 (debe matchear con el establecido en el archivo **Vagrantfile** [```config.vm.network "forwarded_port", guest: 8000, host: 8000```] ) y lo hace disponible a todos los adaptadores de red disponibles mediante **0.0.0.0**

--------------------

## Settings.py

Archivo de configuracion de nuestro proyecto.
Dentro, podemos encontrar un array denominado ***INSTALLED_APPS***, que contendra todas las aplicaciones que utilizara nuestro projecto.

```py
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'profiles_api',
]
```

Comenzaremos activando algunas apps que necesitaremos para este proyecto:

**rest_framework**
: agregamos la dependencia rest_framework de django, la cual necesitaremos en nuestro proyecto.

**rest_framework.authtoken**
: no permitira utilizar la funcionalidad de autenticacion de token que viene con el framework.

**profiles_api**
: por ultimo agregamos nuestra aplicacion.
