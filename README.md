# Curso-PIP-y-Entornos-Virtuales

# Game Project
Este proyecto consta de la recreación en código del juego "Piedra, Papel ó Tijera".
Para correr el juego hay que seguir las siguientes instrucciones en la terminal:

```sh
git clone
cd game
py main.py
```

# App Project
En este proyecto leemos un archivo CSV con el que se genera un gráfico de pastel correspondiente al porcentaje de población mundial, por país, de un determinado continente (para mejorar la visualización).También, se genera un gráfico de barras con la variación poblacional de un país determinado por el usuario, que es guardado dentro de la carpeta 'imgs' que se encuentra dentro de este directorio de trabajo en un archivo con el nombre del país indicado.
Para correr el archivo principal de este proyecto hay que seguir las siguientes instrucciones en la terminal:

```sh
git clone
cd App
py -m venv env-app
. env-app/Script/activate 
pip install -r requirements.txt
py main.py
```

También se puede correr el archivo principal del proyecto, como scrpit, desde un contenedor de Docker al seguir las siguientes instrucciones:

```sh
git clone
cd App
py -m venv env-app
. env-app/Script/activate 
pip install -r requirements.txt
deactivate
docker-compose build
docker-compose up -d
docker-compose ps
docker-compose exec app-csv bash
python main.py
```

Al terminar se recomienda dejar de ejecutar el contenedor con:

```sh
exit
docker-compose down
```

# Charts Project 
Este proyecto genera un gráfico de pastel con valores predeterminados.
Para correr el archivo principal hay que seguir las siguientes instrucciones en la terminal:

```sh
git clone
cd charts
py main.py
```

# Web-server Project
En este proyecto se puede solicitar información de un servidor API correspondiente a un e-commerce (fakeapi.platzi.com), para obtener el nombre de las categorías de artículos que se venden.
Para correr el archivo principal de este proyecto como un script hay que seguir las siguientes instrucciones en la terminal:

```sh
git clone
cd web-server
py -m venv env-web
. env-web/Script/activate 
pip install -r requirements.txt
py main.py
```

También es posible crear y lanzar en línea un servidor web (API), que corra desde un contenedor de Docker, siguiendo las siguientes instrucciones:

```sh
git clone
cd web-server
py -m venv env-web
. env-web/Script/activate 
pip install -r requirements.txt
deactivate
docker-compose build
docker-compose up -d
docker-compose ps
```

Desde el navegador, hay que ingresar a la dirección 'localhost' y/o 'localhost/contact' para ver los resultados del proyecto. Al terminar se recomienda dejar de ejecutar el contenedor con:

```sh
docker-compose down
```

NOTA: Los comando utilizados en estas intrucciones para poder ejecutar los archivos principales de los distintos proyectos corresponden al lenguaje de bash en Windows (Git Bash).