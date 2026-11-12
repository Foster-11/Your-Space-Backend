"""Modelo ORM que mapea reservas a la base de datos."""
from uuid import uuid4 
from sqlalchemy.dialects.postgresql import UUID

import sqlalchemy as sql
import sqlalchemy.orm as orm


from infrastructure.db.base import Base 

#ORM Reservation Model


class ReservationInfrastructureModel(Base):
    __tablename__ = "reservation" # Nombre de la tabla asociada a esta clase.
    id_reservation = sql.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    id_space = sql.Column(
        UUID(as_uuid=True), 
        sql.ForeignKey("space.id_space"), # Referencia a la clave primaria de space.
        nullable=False
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
    expected_attendees = sql.Column(sql.Integer, nullable=False)

    # Relación ORM con el espacio al que pertenece esta reserva.

    space = orm.relationship(
        "Space", # Nombre ORM esperado de la clase mapeada de espacio.
        back_populates="reservations" # Atributo inverso del modelo de espacio.
    )
