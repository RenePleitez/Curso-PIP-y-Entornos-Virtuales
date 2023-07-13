import store
from fastapi import FastAPI #Se importó "FastAPI" de la librería "fastapi".
from fastapi.responses import HTMLResponse # Agregamos la importación que nos permitirá retornar contenido HTML en vez de datos directos en el servidor.


app = FastAPI() # En esta línea creamos nuestro servidor otorgándole un nombre y utilizando la función "FastAPI()" de la librería "fastapi".


@app.get('/') # Sintaxis conocida como decorador, donde especificamos la ruta web cuya respuesta será el recurso establecido dentro del decorador. La ruta establecida corresponde a la ruta principal del servidor creado.
def get_list(): # Creamos el primer recurso, que queremos que sea una función que retorne una lista de valores predeterminados.
    return [1,2,3,] # Respuesta que se mostrará en la ruta establecida en el decorador.


@app.get('/contact', response_class=HTMLResponse) # En este caso el decorador utiliza la palabra clave 'contact' para definir una nueva ruta web (secundaria) donde se mostrará otro recurso establecido dentro de este decorador. Se agregó a este decorador la variable "response_class" para indicar que queremos retornar contenido HTML (HTMLResponse).
def get_list(): # Creamos un segundo recurso, donde podríamos hacer el renderizado de toda una página y agregamos código HTML. La respuesta de este recurso se mostrará como HTML en la ruta establecida en el decorador.
    return """ 
        <h1>Hola soy una página</h1>
        <p>soy un párrafo</p>
"""


def run():
    store.get_categories()


if __name__=='__main__':
    run()