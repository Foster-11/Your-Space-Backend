from domain.exceptions.base import DomainErrorr

class InvalidDateError(DomainErrorr):
    # Se lanza cuando las fechas de la reserva no son válidas (inicio después del fin, fechas pasadas, etc.)
    pass

class SpaceNotExistsError(DomainErrorr):
    # Se lanza cuando se intenta reservar un espacio que no existe
    pass

class OverlappingReservationError(DomainErrorr):
    # Se lanza cuando se intenta crear una reserva que se solapa con otra existente
    pass

class ExceedCapacityError(DomainErrorr):
    # Se lanza cuando se intenta crear una reserva que excede la capacidad del espacio
    pass

class ReservationNotFound(DomainErrorr):
    # Se lanza cuando se intenta acceder a una reserva que no existe
    pass

class ReservationCancellationWindowExpiredError(DomainErrorr):
    # Se lanza cuando La ventana de cancelación expiró.
    pass