# routers/ : expone endpoints de cada entidad

# reservation_router.py : recibe request, valida datos con shemas y llama al servicio correspondiente

from fastapi import APIRouter, HTTPException, status

from api.schemas import (
    ReservationCreateSchema,
    ReservationResponseSchema,
)
from domain.services.reservation_service import create_reservation

router = APIRouter(prefix="/reservations", tags=["Reservations"])


@router.post(
    "",
    response_model=ReservationResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_reservation_endpoint(payload: ReservationCreateSchema):
    try:
        reservation = create_reservation(
            reservation_repo=None,  # infrastructure luego
            space_repo=None,        # infrastructure luego
            id_space=payload.id_space,
            start_datetime=payload.start_datetime,
            end_datetime=payload.end_datetime,
            event_name=payload.event_name,
            client_name=payload.client_name,
            clien_email=payload.client_email,
        )
        return reservation

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


@router.get("/{reservation_id}", response_model=ReservationResponseSchema)
def get_reservation(reservation_id: str):
    return {
        "id_reservation": reservation_id,
        "id_space": reservation_id,
        "start_datetime": "2026-01-01T00:00:00",
        "end_datetime": "2026-01-01T01:00:00",
        "event_name": "",
        "client_name": "",
        "client_email": ""
    }


@router.get("", response_model=list[ReservationResponseSchema])
def list_reservations():
    return []


@router.delete("/{reservation_id}", status_code=204)
def cancel_reservation(reservation_id: str):
    return None

