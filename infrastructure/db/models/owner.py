
"""Modelo ORM que mapea propietarios a la tabla correspondiente."""

# infrastructure/db/models/owner.py
from uuid import uuid4 
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as sql
import sqlalchemy.orm as orm

from infrastructure.db.base import Base 

# ORM Owner Model

class OwnerInfrastructureModel(Base):
    __tablename__ = "owner" # Nombre de la tabla asociada a esta clase.
    id_owner = sql.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = sql.Column(sql.String(100), index=True, nullable=False) # El índice puede acelerar búsquedas por nombre.
    last_name = sql.Column(sql.String, index=True, nullable=False)
    email = sql.Column(sql.String, unique=True, index=True, nullable=False) # La base impide emails duplicados.
    password = sql.Column(sql.String, nullable=False) 

    # Relación ORM con los espacios de este propietario.
    spaces = orm.relationship(
        "Space", # Nombre ORM esperado de la clase mapeada en el módulo de espacios.
        back_populates="owner", # Atributo inverso declarado en el modelo de espacio.
        cascade="all, delete-orphan" # Al borrar al propietario por el ORM, también borra sus espacios.
    )


