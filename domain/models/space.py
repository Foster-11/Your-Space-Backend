# domain/ : Razon de ser del sistema, nucleo del negocio testeable
# ../models/: Entidades del negocio, no son tablas sino conceptos del negocio
# space.py : un salón que pertenece a un propietario

# Space.py
from uuid import uuid4 
from sqlalchemy.dialects.postgresql import UUID

import sqlalchemy as sql
import sqlalchemy.orm as orm

from infrastructure.db.base import Base


class Space(Base):
    __tablename__ = "space" # Nombre de la tabla en la bd
    id_space = sql.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    id_owner = sql.Column(
        UUID(as_uuid=True), # Qué es?
        sql.ForeignKey("owner.id_owner"), # 'owner' es el nombre real de la tabla
        nullable=False
        )
    name = sql.Column(sql.String(100), index=True, nullable=False) # index para busquedas rapidas
    description = sql.Column(sql.String, index=True, nullable=True)
    capacity = sql.Column(sql.Integer, index=True, nullable=False)
    
    # Relaciones
    owner = orm.relationship(
        "Owner", # Nombre de la clase
        back_populates="spaces" 
    )

    reservation = orm.relationship( #vinculo visto en reservation.py
        "Reservation", # nombre de la clase
        back_populates="space", 
        cascade="all, delete-orphan" # si se borra space, se borran todas sus reservas
    )
