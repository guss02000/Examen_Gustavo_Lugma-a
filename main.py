from fastapi import FastAPI
from pydantic import BaseModel
from classifier import clasificar_mensaje

app = FastAPI()

class Mensaje(BaseModel):
    texto: str
    
@app.post("/clasificar/")
def clasificar(mensaje: Mensaje):
    resultado = clasificar_mensaje(mensaje.texto)
    return resultado