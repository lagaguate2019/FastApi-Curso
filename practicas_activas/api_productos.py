"""
Fecha: 2023-01-16
Tutorial: Crear CRUD, con fastAPI
"""

from fastapi import FastAPI
from pydantic import BaseModel

"""
Defincion de modelo productos
"""
class Producto (BaseModel):
    id: Optional [str]

app = FastAPI()

@app.get("/")
def index():
    return {'index':'Bienvenidos - API Products'}
