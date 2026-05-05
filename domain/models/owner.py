# domain/ : Razon de ser del sistema, nucleo del negocio testeable
# owner.py : propietario de un salon o varios salones
# ../models/: Entidades del negocio, no son tablas sino conceptos del negocio 

# ORM con estilo de consulta Core con SQLAlchemy
# ORM: Object Relational Mapping,  técnica de programación utilizada para convertir datos 
# entre sistemas de tipos incompatibles en lenguajes de programación orientados a objetos y bases de datos relacionales

# owner.py
from uuid import uuid4 
from sqlalchemy.dialects.postgresql import UUID

import sqlalchemy as sql
import sqlalchemy.orm as orm

from infrastructure.db.base import Base 

class Owner(Base):
    __tablename__ = "owner" # nombre de la tabla en la bd
    id_owner = sql.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = sql.Column(sql.String(100), index=True, nullable=False) # index=True crea un indice para busquedas rapidas
    last_name = sql.Column(sql.String, index=True, nullable=False)
    email = sql.Column(sql.String, unique=True, index=True, nullable=False) #unique : restriccion para la bd
    password = sql.Column(sql.String, nullable=False) 

    #Relaciones
    spaces = orm.relationship(
        "Space", # nombre de la clase en space.py
        back_populates="owner", # relacion inversa en space
        cascade="all, delete-orphan" # si elimina owner, se eliminan sus espacios
    )



