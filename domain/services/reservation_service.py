# domain/ : Razon de ser del sistema, nucleo del negocio testeable
# ../services/: logica real,  reglas del negocio, lanzamiento de excepciones (fail fast + graceful handling)
# reservation_service.py : reglas para las reservas en el sistema - Entidad núclep

# domain/services/reservation_service.py

# Respondabilidades clave:
# 1. crear una reserva - check
# 2. Validar que exista space - check
# 3. validar solapamientos de fechas - check
# 4. validar fechas coherentes (overlapping, dont create reserve for past) - check
# 5. validar capacidad del espacio con la reserva - check
# 6. cancelar reserva (o sea, eliminar una reserva existente)
# 7. listar reservas de un space sin vencer
# 8. listar reservas por cliente sin vencer
# 9. listar reservas ya vencidas de un space
# 10 listar reservas totales de un space

from domain.models.reservation import Reservation
from domain.exceptions.reservation import (
    InvalidDateError,
    SpaceNotExistsError,
    OverlappingReservationError,
    ExceedCapacityError,
    ReservationNotFound,
    ReservationCancellationWindowExpiredError
)

def create_reservation(
        *, # Keyword-only: contrato claro del servicio
        reservation_repo, # Repo de Reservation, encapsula queries
        # (ej: exists_overlap, add)

        space_repo, # Se usa para validar que el space exista
        id_space,
        start_datetime,
        end_datetime,
        event_name,
        event_description,
        client_name,
        client_email,
        expected_attendees
        ):
    
    if end_datetime  <= start_datetime: #Regla de negocio
        raise InvalidDateError("El inicio de la reserva debe estar antes que el fin de la reserva")
    
    space = space_repo.get_space_by_id(id_space)
    if not space: #No se puede reservar en space inexistente
        raise SpaceNotExistsError("Space no encontrado")
    
    overlapping = reservation_repo.exists_overlap(
        id_space, 
        start_datetime, 
        end_datetime
    )
    if overlapping: #Regla crítica del dominio
        raise OverlappingReservationError("El espacio ya está reservado para esta fecha y hora")
    
    if expected_attendees > space.capacity:
        raise ExceedCapacityError("El número de asistentes esperados excede la capacidad del espacio")
    
    reservation = Reservation( #Se crea la entidad del dominio
        id_space = id_space,
        start_datetime = start_datetime,
        end_datetime = end_datetime,
        client_name = client_name,
        client_email = client_email,
        event_name = event_name,
        event_description = event_description,
        expected_attendees = expected_attendees
    )
    reservation_repo.add(reservation)
    
    return reservation

# Restricción: No se puede cancelar en menos de 24 horas de la hora de la reserva
def cancel_reservation(
        *,
        reservation_repo,
        reservation_id,
        current_datetime
):
    reservation = reservation_repo.get_reservation_by_id(reservation_id)
    if not reservation:
        raise ReservationNotFound("Reserva no encontrada")

    if reservation.start_datetime - current_datetime < timedelta(hours=24):
        raise ReservationCancellationWindowExpiredError("La ventana de cancelación expiró")

    reservation_repo.delete_reservation_by_id(reservation_id)