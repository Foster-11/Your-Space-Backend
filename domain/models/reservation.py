# domain/ : Razon de ser del sistema, nucleo del negocio testeable
# ../models/: Entidades del negocio, no son tablas sino conceptos del negocio
# reservation.py : Una reserva de un salón 

# reservation.py
from uuid import uuid4 
from sqlalchemy.dialects.postgresql import UUID

import sqlalchemy as sql
import sqlalchemy.orm as orm
from datetime import datetime

from infrastructure.db.base import Base 




class Reservation(Base):
    __tablename__ = "reservation" #Nombre de la tabla en la BD
    id_reservation = sql.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    id_space = sql.Column(
        UUID(as_uuid=True), 
        sql.ForeignKey("space.id_space"), #'space' es el nombre de la tabla en la bd
        nullable=False # not null
        )
    id_state = sql.Column(
        sql.Integer,
        nullable=False
    )
    start_datetime = sql.Column(
        sql.DateTime,
        nullable=False
    )
    end_datetime = sql.Column(
        sql.DateTime,
        nullable=False
    )
    event_name = sql.Column(sql.String(100), nullable=False)
    event_description = sql.Column(sql.String(255), nullable=True)
    client_name = sql.Column(sql.String(255), nullable=False)
    client_email = sql.Column(sql.String(120), nullable=False)

    # Relaciones

    space = orm.relationship(
        "Space", # nombre de la clase
        back_populates="reservation" # vincula la relacion con Space.reservation
    )
