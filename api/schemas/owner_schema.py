# schemas/ : Contratos HTTP PARA VALIDAR INPUTS, DOCUMENTAR LA apia y serializar outputs

#owner_schema.py
"""
Expone:
1. crear un nuevo owner
2. login
3. responder owner sin password
"""


from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

# Request

class OwnerCreateSchema(BaseModel):
    name: str = Field(..., min_length=1) # el ... indica que es obligatorio, min_length=1 para que no sea una cadena vacía
    last_name: str = Field(..., min_length=1)
    email: EmailStr
    password: str = Field(..., min_length=6)


class OwnerLoginSchema(BaseModel):
    email: EmailStr
    password: str


# Response

class OwnerResponseSchema(BaseModel):
    id_owner: UUID
    name: str
    last_name: str
    email: EmailStr

    class Config:
        from_attributes = True # Permite crear una instancia de OwnerResponseSchema a partir de un objeto que tenga atributos con los mismos nombres (como un modelo de SQLAlchemy)  permite devolver modelos del dominio sin acoplarlos a la capa de presentación.
    
