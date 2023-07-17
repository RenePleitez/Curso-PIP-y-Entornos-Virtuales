FROM python:3.10
# Se definió que la versión de Python de este contenedor sea la 3.10
WORKDIR /web-server
COPY requirements.txt /web-server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /web-server/requirements.txt

COPY . /web-server

#El cambio en este comando tiene que ver con que en vez de dejar encendido el contenedor para poder conctarnos y ejecutar scripts, vamos a lanzar directamente el servidor de "uvicorn" (que es el que mantiene prendido nuestro servidor en con la librería de Python "fastapi").
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 
# Creamos una lista dentro del comando que contendrá las instrucciones. Primero, indicamos que se ejecute "uvicorn" y se ingrese al módulo "main" donde a su vez se llama a la aplicación "app" (que es el nombre de nuestro servidor). Luego, ponemos el "--host" que determinamos sea el puerto "0.0.0.0" y, finalmente, determinamos que el puerto "--port" en el que va a correr sea el "8000" (puerto en el que normalmente corre, pero también puede correr en otro puerto de preferencia).