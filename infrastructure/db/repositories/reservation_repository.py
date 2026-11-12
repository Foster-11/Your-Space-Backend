# ../repositories/: se escriben queries, se usan sesiones y se ejecuta sql
# ../repositories/: queries, sesiones y traducción dominio <-> ORM
# Adaptador SQLAlchemy que traduce entre objetos de dominio y modelos ORM.
from sqlalchemy import exists, select
from sqlalchemy.orm import Session

from domain.models.reservation import Reservation
from infrastructure.db.models import ReservationModel


def _to_domain(model: ReservationModel) -> Reservation:
    return Reservation(
        id_reservation=model.id_reservation,
        id_space=model.id_space,
        id_state=model.id_state,
        start_datetime=model.start_datetime,
        end_datetime=model.end_datetime,
        event_name=model.event_name,
        event_description=model.event_description,
        client_name=model.client_name,
        client_email=model.client_email,
        expected_attendees=model.expected_attendees,
    )


def _to_model(reservation: Reservation) -> ReservationModel:
    return ReservationModel(
        id_reservation=reservation.id_reservation,
        id_space=reservation.id_space,
        id_state=reservation.id_state,
        start_datetime=reservation.start_datetime,
        end_datetime=reservation.end_datetime,
        event_name=reservation.event_name,
        event_description=reservation.event_description,
        client_name=reservation.client_name,
        client_email=reservation.client_email,
        expected_attendees=reservation.expected_attendees,
    )


class SqlAlchemyReservationRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, reservation: Reservation) -> None:
        self.session.add(_to_model(reservation))
        self.session.commit()

    def get_reservation_by_id(self, id_reservation) -> Reservation | None:
        model = self.session.get(ReservationModel, id_reservation)
        return _to_domain(model) if model else None

    def exists_overlap(self, id_space, start_datetime, end_datetime) -> bool:
        stmt = select(
            exists().where(
                ReservationModel.id_space == id_space,
                ReservationModel.start_datetime < end_datetime,
                ReservationModel.end_datetime > start_datetime,
            )
        )
        return bool(self.session.scalar(stmt))

    def delete_reservation_by_id(self, id_reservation) -> bool:
        model = self.session.get(ReservationModel, id_reservation)
        if not model:
            return False
        self.session.delete(model)
        self.session.commit()
        return True