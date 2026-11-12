# schemas/ : Contratos HTTP PARA VALIDAR INPUTS, DOCUMENTAR La API y serializar outputs
# Traducir entre el mundo HTTP y el dominio.

# api/schemas/owner_schema.py
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
    name: str = Field(..., min_length=1) # ... lo hace obligatorio y min_length exige al menos un carácter.
    last_name: str = Field(..., min_length=1)
    email: EmailStr
    password: str = Field(..., min_length=6)


class OwnerLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)




# Response
class OwnerResponseSchema(BaseModel):
    id_owner: UUID
    name: str
    last_name: str
    email: EmailStr

    class Config:
        from_attributes = True # Permite construir la respuesta desde atributos del objeto de dominio.
    
