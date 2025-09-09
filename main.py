#Ejecutar "uvicorn --port 8000 --reload --log-level info main:app" en Powershell para correr Uvicorn, el servidor web que se comunicará con la API para pasar y responder solicitudes de clientes http o https.
#"from typing import Union" Se remplazó por el uso del operador "|" admitido en versiones superiores a Python 10.
from fastapi import FastAPI
from models.item_model import Item #Se vincula la clase Item de modulo "models"


#Creación de una aplicación mediante una instancia de FastAPI()
app = FastAPI()

#Método GET para retornar la respuesta de la función ... al cliente HTPSS, sin modificar los datos del recurso.

#Función holamundo
@app.get('/')
def holamundo():
    return {'!Hola123':'Mundo'}

#Función leer_items, que emplea parámetros de ruta y consulta
#Ejemplo para el navegador: localhost:8000/items/1000?q=Mouse
@app.get('/items/{item_id}')
def leer_items(item_id:int, q:str|None=None):
    return {"item_id":item_id, "q":q}

#Función sumar_operandos, que emplea parámetros de consulta
#Ejemplo para el navegador: localhost:8000/suma?operando_1=5&operando_2=7
@app.get('/suma')
def sumar_operandos(operando_1:int, operando_2:int):
    return {'suma':operando_1+operando_2}

#Método PUT para actualizar los datos del recurso mediante la función ... que respeta esquemas de clase.

#Función actualizar_item
#Se probó su funcionamiento en la página de la documentación generada por FastAPI
@app.put('/item/{item_id}')
def actualizar_item(item_id:int, item: Item):
    return {'item_id':item_id,
            'name':item.name,
            'is_offer':item.is_offer}