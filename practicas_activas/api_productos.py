"""
Fecha: 2023-01-16
Tutorial: Crear CRUD, con fastAPI
"""

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4 as uuid
"""
Defincion de modelo productos
"""
class Producto (BaseModel):
    id: Optional [str]
    nombre: str
    precio_venta: float
    precio_compra: float
    proveedor: str

app = FastAPI()

productos = []

@app.get("/")
def index():
    return {'index':'Bienvenidos - API Products'}

@app.get("/producto")
def getProducto():
    return productos

@app.post("/producto")
def crear_producto (producto: Producto):
    producto.id = str(uuid())
    productos.append(producto)
    return {'message':'Creado'}
