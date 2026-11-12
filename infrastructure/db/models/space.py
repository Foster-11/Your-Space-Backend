"""Modelo ORM que mapea espacios y sus relaciones de persistencia."""
from uuid import uuid4 
from sqlalchemy.dialects.postgresql import UUID

import sqlalchemy as sql
import sqlalchemy.orm as orm

from infrastructure.db.base import Base

# ORM Space Model
class SpaceInfrastructureModel(Base):
    __tablename__ = "space" # Nombre de la tabla asociada a esta clase.
    id_space = sql.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    id_owner = sql.Column(
        UUID(as_uuid=True),
        sql.ForeignKey("owner.id_owner"), # Referencia a la clave primaria de owner.
        nullable=False
        )
    name = sql.Column(sql.String(100), index=True, nullable=False) # El índice puede acelerar búsquedas por nombre.
    description = sql.Column(sql.String, index=True, nullable=True)
    capacity = sql.Column(sql.Integer, index=True, nullable=False)
    
    # Relaciones ORM; los nombres de destino deben coincidir con las clases mapeadas.
    owner = orm.relationship(
        "Owner", # Nombre ORM esperado de la clase mapeada de propietario.
        back_populates="spaces" # Atributo inverso en el modelo de propietario.
    )


    reservations = orm.relationship(
        "Reservation", # Nombre ORM esperado de la clase mapeada de reserva.
        back_populates="space",
        cascade="all, delete-orphan" # Al borrar el espacio por el ORM, también borra sus reservas.
    )
