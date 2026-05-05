# domain/exceptions/owner.py

# qué son las excepciones y para qué sirven? 

from domain.exceptions.base import DomainError

class OwnerAlreadyExistError(DomainError):
    # Se lanza cuando el email ya existe
    pass


class InvalidCredentialsError(DomainError):
    # Credenciales no validas
    pass

class OwnerNotFound(DomainError):
    # No se encuentra el owner solicitado
    pass
