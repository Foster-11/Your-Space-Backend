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
    name: str = Field(..., min_length=1) # Es obligatorio y debe tener al menos un carácter.
    description: str | None = None # La descripción es opcional.
    capacity: int = Field(..., gt=0) # Es obligatoria y debe ser mayor que cero.

# Response
class SpaceResponseSchema(BaseModel):
    id_space: UUID
    id_owner: UUID
    name: str
    description: str | None # La respuesta puede no incluir una descripción.
    capacity: int

    class Config: 
        from_attributes = True # Permite construir la respuesta desde atributos del objeto de dominio.