
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

La estructura de django es: root/project_name contendra todos los archivos base del proyecto, como ser **settings**, **urls** y **wsgi**. Luego, pueden existir n apps por projecto y siempre su nomenclatura es <project_name>/appname. En este caso **profiles_projects** es nuestro directorio de proyecto y nuestra app es **profiles_api**, que como se puede apreciar, primero contiene el nombre del projecto y luego el de la app

### Se nos creara el siguiente directorio que contendra la app

![app init](readme_imgs\django_app_script.py.png)

```sh
    python manage.py runserver 0.0.0.0:8000
```

> Ejecutamos el script manage.py y le indicamos que queremos correr el servidor con el comando **runserver**, en este caso, en el puerto 8000 (debe matchear con el establecido en el archivo **Vagrantfile** [```config.vm.network "forwarded_port", guest: 8000, host: 8000```] ) y lo hace disponible a todos los adaptadores de red disponibles mediante **0.0.0.0**

--------------------

## Settings

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

### Como setear un modelo custom

Dentro de nuestro archivo settings.py, agregamos la siguiente linea

```py
    AUTH_USER_MODEL = 'profiles_api.UserProfile
```

Le especificamos a django que el modelo contenido dentro de profiles_api, sera el modelo que utilizara para la autenticacion y registros de toda la app.

De esta manera se configura un modelo en django

--------------------

## Models

--------------------

En este archivo se crean los modelos que utilizara nuestra aplicacion.

```py
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)
from django.db import models


class UserProfileManager(BaseUserManager):
    """
        Manager for user profiles
    """
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # This method is inherited from AbstractBaseUser class and it hash the password
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
        Database model for users in the system
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # Cuando se autentiquen, mediante este metodo indicamos que en lugar de utilizar el nombre de la
    # persona, utilizara el campo email como usuario
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
            Retrieve full name of user
        """
        return self.name

    def get_short_name(self):
        """
            Retrieves short name of the user
        """
        return self.name

    def __str__(self):
        """
            Return string representation of our user
        """
        return self.email

```

## Migrations

La manera en la que django maneja la base de datos es creando un archivo *migration* que contenga todos los pasos requeridos para que nuestra base de datos matchee con nuestros modelos. Por lo cual, cada vez que creamos o modificamos un modelo, debemos crear o actualizar el archivo migration

Serian como nuestro ORM.

El siguiente comando creara por nosotros los migrations para los modelos de nuestra app
:

```sh
    python manage.py makemigrations profiles_api
```

Para correr todos los migrations de nuestro proyecto utilizamos el siguiente comando:

```sh
    python manage.py migrate
```
