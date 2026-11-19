# infrastructure/ : Detalles tecnicos
# ../base.py : Base SQLAlchemy


# infrastructure/db/base.py
from sqlalchemy.orm import DeclarativeBase
"""
DeclarativeBase es una clase proporcionada por SQLAlchemy que sirve como punto de partida para 
definir modelos ORM (Ver documentación en este repo: infrastructure\README.md)
"""

class Base(DeclarativeBase):
    pass