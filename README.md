# LABSMATE
Esta es una actividad diseñada por el Profesor Jimmy Villegas.

## Instalación

Asegúrate de tener **python** instalado y es preferible usar un virtual enviroment. 
Para instalarlo puedes hacerlo ejecutando los siguientes comandos:

1. Instala las dependencias con los comandos:

```bash
pip install -r requirements.txt
```

2. Realiza las migraciones necesarias con los comandos:

```bash
python manage.py makemigrations
python manage.py migrate
```

3. Ahora, inicia el servidor local:

```bash
python manage.py runserver
```

El programa debe estar escuchando en el puerto 8000 y puedes acceder a él escribiendo este codigo en tu explorador `http://localhost:8000`.

## Compatibilidad con Docker

He incluido un **Dockerfile** en la carpeta raíz para ejecutar esta actividad en entornos Dockerizados.

1. Asegúrate de tener Docker instalado en tu máquina.
2. Navega hasta el directorio raíz del proyecto.
3. Ejecuta el siguiente comando para construir la imagen de Docker:

```bash
docker build -t labsmate .
```

4. Una vez que la imagen esté lista, puedes iniciar tu contenedor con:

```bash
docker run --rm --name labsmate -p 8000:8000 labsmate
```

Ahora puedes acceder al proyecto a través de `http://localhost:8000` incluso con Docker.

## Pruebas Unitarias

He incorporado pruebas unitarias, para ejecutar las pruebas ejecuta:

```bash
python manage.py test
```

## Gracias por leer

Si tienes preguntas, no dudes en ponerte en contacto [deiby.rodriguez@correounivalle.edu.co](mailto:deiby.rodriguez@correounivalle.edu.co).