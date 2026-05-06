# schemas/ : Contratos HTTP PARA VALIDAR INPUTS, DOCUMENTAR LA apia y serializar outputs
# reservation_schema.py
"""
Expone:
1. crear una nueva reserva
2. validar rangos de fechas para evitar solapamientos
3. Listar reservas
"""

from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field

# Request

class ReservationCreateSchema(BaseModel):
    id_space: UUID
    start_datetime: datetime
    end_datetime: datetime
    event_name: str = Field(..., min_length=1) # el ... indica que es obligatorio, min_length=1 para que no sea una cadena vacía
    client_name: str = Field(..., min_length=1) # el ... indica que es obligatorio, min_length=1 para que no sea una cadena vacía
    client_email: str

    class Config: # Permite agregar ejemplos a la documentación de la API, lo que facilita a los desarrolladores entender cómo usar el endpoint y qué tipo de datos se espera en la solicitud.
        json_schema_extra = {
            "example": {
                "id_space": "550e8400-e29b-41d4-a716-446655440000",
                "start_datetime": "2026-04-20T10:00:00",
                "end_datetime": "2026-04-20T12:00:00",
                "event_name": "Reunión de proyecto",
                "client_name": "Juan Pérez",
                "client_email": "juan@test.com"
            }
        }

# Response
class ReservationResponseSchema(BaseModel):
    id_reservation: UUID
    id_space: UUID
    start_datetime: datetime
    end_datetime: datetime
    event_name: str
    client_name: str
    client_email: str

    class Config: # Permite crear una instancia de ReservationResponseSchema a partir de un objeto que tenga atributos con los mismos nombres (como un modelo de SQLAlchemy)  permite devolver modelos del dominio sin acoplarlos a la capa de presentación.
        from_attributes = True

