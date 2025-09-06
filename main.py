from typing import Union
from fastapi import FastAPI

#Creación de una aplicación mediante una instancia de FastAPI()
app = FastAPI()

#Método GET para retornar la respuesta de la función ... al cliente HTPSS

#Función holamundo
@app.get('/')
def holamundo():
    return {'!Hola23':'Mundo'}