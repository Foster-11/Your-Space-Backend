# domain/ : Razon de ser del sistema, nucleo del negocio testeable
# ../services/: logica real,  reglas del negocio, lanzamiento de excepciones (fail fast + graceful handling)
# reservation_service.py : reglas para las reservas en el sistema - Entidad núclep

#reservation_service.py

# Respondabilidades clave:
# 1. crear una reserva - check
# 2. Validar que exista space - check
# 3. validar solapamientos de fechas - check
# 4. validar fechas coherentes (overlapping, dont create reserve for past) - pending
# 5. cancelar reserva - pending
# 6. listar reservas de un space - pending

from domain.models.reservation import Reservation

def create_reservation(
        *, # Keyword-only: contrato claro del servicio
        reservation_repo, # Repo de Reservation, encapsula queries
        # (ej: exists_overlap, add)

        space_repo, # Se usa para validar que el space exista
        id_space,
        start_datetime,
        end_datetime,
        event_name,
        client_name,
        clien_email
        ):
    
    if start_datetime >= end_datetime: #Regla de negocio
        raise ValueError("El inicio de la reserva debe estar antes que el fin de la reserva")
    
    space = space_repo.get_by_id(id_space)
    if not space: #No se puede reservar en space inexistente
        raise ValueError("Space no encontrado")
    
    overlapping = reservation_repo.exists_overlap(
        id_space, 
        start_datetime, 
        end_datetime
    )
    if overlapping: #Regla crítica del dominio
        raise ValueError("El espacio ya está reservado para esta fecha y hora")
    
    reservation = Reservation( #Se crea la entidad del dominio
        id_space = id_space,
        start_datetime = start_datetime,
        end_datetime = end_datetime,
        client_name = client_name,
        client_email = clien_email,
        event_name = event_name
    )
    reservation_repo.add(reservation)
    
    return reservation
