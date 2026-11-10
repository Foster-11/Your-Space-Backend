# domain/models/reservation.py : una reserva de un salón
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(kw_only=True)
class Reservation:
    id_space: UUID
    start_datetime: datetime
    end_datetime: datetime
    event_name: str
    client_name: str
    client_email: str
    expected_attendees: int
    event_description: str | None = None
    id_state: int | None = None
    id_reservation: UUID = field(default_factory=uuid4)