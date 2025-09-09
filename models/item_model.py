from pydantic import BaseModel #Se importa la clase BaseModel para realizar una solicitud de tipo PUT

#Creación de la clase Item a partir de BaseModel que servirá como esquema para actualizar items mediante solicitudes PUT
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool|None=None