"""Casos de uso actuales para crear y cancelar reservas."""

from domain.models.reservation import ReservationDomainModel
from domain.exceptions.reservation import (
    InvalidDateError,
    SpaceNotExistsError,
    OverlappingReservationError,
    ExceedCapacityError,
    ReservationNotFound,
    ReservationCancellationWindowExpiredError
)

def create_reservation(
        *, # Hace obligatorio pasar las dependencias y datos por nombre.
        reservation_repo, # Busca solapamientos y guarda o consulta reservas.

        space_repo, # Busca el espacio y permite comprobar su capacidad.
        id_space,
        start_datetime,
        end_datetime,
        event_name,
        event_description,
        client_name,
        client_email,
        expected_attendees
        ):
    
    if end_datetime <= start_datetime: # El intervalo debe tener duración positiva.
        raise InvalidDateError("El inicio de la reserva debe estar antes que el fin de la reserva")
    
    space = space_repo.get_space_by_id(id_space)
    if not space: # Una reserva debe pertenecer a un espacio existente.
        raise SpaceNotExistsError("Space no encontrado")
    
    overlapping = reservation_repo.exists_overlap(
        id_space, 
        start_datetime, 
        end_datetime
    )
    if overlapping: # El mismo espacio no puede tener reservas solapadas.
        raise OverlappingReservationError("El espacio ya está reservado para esta fecha y hora")
    
    if expected_attendees > space.capacity:
        raise ExceedCapacityError("El número de asistentes esperados excede la capacidad del espacio")
    
    reservation = ReservationDomainModel( # Crea el objeto de dominio, independiente del ORM.
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

# La cancelación está permitida solo si faltan al menos 24 horas para el inicio.
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