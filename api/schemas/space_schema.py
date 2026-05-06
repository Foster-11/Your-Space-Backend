# schemas/ : Contratos HTTP PARA VALIDAR INPUTS, DOCUMENTAR LA apia y serializar outputs

# space_schema.py
"""
Expone:
1. crear un nuevo space
2. Listar spaces
"""

from uuid import UUID
from pydantic import BaseModel, Field

# Request

# El ownership se maneja por id_owner
# La API no necesita cargar el Owner completo aquí
class SpaceCreateSchema(BaseModel):
    id_owner: UUID
    name: str = Field(..., min_length=1) # el ... indica que es obligatorio, min_length=1 para que no sea una cadena vacía
    description: str | None = None # el espacio de descripción es opcional, por eso se le asigna un valor por defecto de None
    capacity: int = Field(..., gt=0) # el ... indica que es obligatorio, gt=0 para que la capacidad sea un número entero positivo

# Response
class SpaceResponseSchema(BaseModel):
    id_space: UUID
    id_owner: UUID
    name: str
    description: str | None # el espacio de descripción es opcional, por eso se le asigna un valor por defecto de None
    capacity: int

    class Config: 
        from_attributes = True # Permite crear una instancia de SpaceResponseSchema a partir de un objeto que tenga atributos con los mismos nombres (como un modelo de SQLAlchemy)  permite devolver modelos del dominio sin acoplarlos a la capa de presentación.