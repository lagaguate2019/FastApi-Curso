"""
Fecha: 2023-01-16
Tutorial: Crear CRUD, con fastAPI
"""

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

"""
Defincion de modelo productos
"""
class Producto (BaseModel):
    id: Optional [str]
    nombre: str
    precio_venta: float
    precio_compra:float
    proveedor: str

app = FastAPI()

@app.get("/")
def index():
    return {'index':'Bienvenidos - API Products'}
