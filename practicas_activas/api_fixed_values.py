# Definir en un api una lista de valores
# Buena practica:  Se definen al principio las lib estandar.
from enum import Enum
from fastapi import FastAPI

class ModelName (str, Enum):
    pais1 = "Guatemala"
    pais2 = "Costa Rica"
    pais3 = "Honduras"

app = FastAPI()

@app.get ("/model/{modelname}")
async def getModel (modelname: ModelName):
    if modelname is ModelName.pais1:
        return {'modelname':modelname, 'message':f'Opcion1 pais1 {modelname.pais1}'} 
    
    if modelname.name=="Costa Rica":
        return {'modelname':modelname, 'message':f'Opcion2 pais2 {modelname.pais2}'} 

    return {'modelname':modelname, 'message':f'Opcion3 Entonces pais3 {modelname.pais3}'} 
