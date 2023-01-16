"""
Fecha: 2023-01-16
Tutorial: Crear CRUD, con fastAPI
"""

from typing import Optional
from fastapi import FastAPI, HTTPException
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

@app.get("/productos")
def getProductos():
    return productos

@app.post("/producto")
def crear_producto (producto: Producto):
    producto.id = str(uuid())
    productos.append(producto)
    return {'message':'Creado'}


## Busqueda por for, if
@app.get("/producto/{id}")
def getProductoPorId(producto_id: str):
    for p in productos:
        if p.id == producto_id:
            return p

    return {'mensaje':f'No existe id {producto_id}'} 

## Busqueda por funcion filter  
@app.get('/productofilter/{id}')
def getProductoPorId_filter (id:str):
    result = list(filter (lambda p: p.id == id, productos))

    if len(result):
        return result

    raise HTTPException(status_code=404,detail=f'No existe id {id}')

 ## Borar Id
@app.delete('/producto/{id}')
def borrarId (id:str):
    result = list(filter (lambda p: p.id == id, productos))

    if len(result):
        producto = result[0]
        productos.remove(producto)
        return {'mensaje':f'{id}, eliminado'}

    raise HTTPException(status_code=404,detail=f'No existe id {id}')


