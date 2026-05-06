from domain.exceptions.base import DomainError


class OwnerAlreadyExistsError(DomainError):
    # Se lanza cuando el email ya existe
    pass


class InvalidCredentialsError(DomainError):
    # Credenciales no válidas
    pass


class OwnerNotFoundError(DomainError):
    # No se encuentra el owner solicitado
    pass