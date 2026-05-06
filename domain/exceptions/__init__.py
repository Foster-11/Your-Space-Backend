# domain/exceptions/__init.py

# __init__.py indica que LA CARPETA es un paquete de python
# permite importar las excepciones de forma limpia



from domain.exceptions.base import DomainError
from domain.exceptions.owner import (
    OwnerAlreadyExistsError,
    InvalidCredentialsError,
    OwnerNotFoundError,
)

__all__ = [
    "DomainError",
    "OwnerAlreadyExistsError",
    "InvalidCredentialsError",
    "OwnerNotFoundError",
]

