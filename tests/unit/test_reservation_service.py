import pytest
from datetime import datetime, timedelta
import uuid

from domain.services.reservation_service import create_reservation
from domain.models.space import Space
from domain.repositories.fakes import FakeReservationRepository, FakeSpaceRepository


#test 1: Creación exitosa de una reserva
def test_create_reservation_successfully():
    space_repo = FakeSpaceRepository()
    reservation_repo = FakeReservationRepository()

    space = Space(
        id_space=uuid.uuid4(),
        id_owner=uuid.uuid4(),
        name="Sala A",
        description="Sala principal",
        capacity=50
    )
    space_repo.add(space)

    start = datetime.now() + timedelta(hours=1)
    end = start + timedelta(hours=2)

    reservation = create_reservation(
        reservation_repo=reservation_repo,
        space_repo=space_repo,
        id_space=space.id_space,
        start_datetime=start,
        end_datetime=end,
        event_name="Evento",
        client_name="Cliente",
        clien_email="cliente@test.com"
    )

    assert reservation is not None
    assert reservation.id_space == space.id_space
    assert reservation.event_name == "Evento"
    assert reservation.client_name == "Cliente"
    assert reservation.client_email == "cliente@test.com"

#test 2: Creación de una reserva con espacio no existente
def test_create_reservation_space_not_found():
    space_repo = FakeSpaceRepository()
    reservation_repo = FakeReservationRepository()

    start = datetime.now() + timedelta(hours=1)
    end = start + timedelta(hours=2)

    with pytest.raises(ValueError):
        create_reservation(
            reservation_repo=reservation_repo,
            space_repo=space_repo,
            id_space=uuid.uuid4(),
            start_datetime=start,
            end_datetime=end,
            event_name="Evento",
            client_name="Cliente",
            clien_email="cliente@test.com"
        )

#test 3: Creación de una reserva con fechas inválidas (end antes de start)
def test_create_reservation_overlapping():
    space_repo = FakeSpaceRepository()
    reservation_repo = FakeReservationRepository()

    space = Space(
        id_space=uuid.uuid4(),
        id_owner=uuid.uuid4(),
        name="Sala A",
        description="Sala principal",
        capacity=50
    )
    space_repo.add(space)

    start = datetime.now() + timedelta(hours=1)
    end = start + timedelta(hours=2)

    reservation_repo.overlapping = True  # simulamos solapamiento

    with pytest.raises(ValueError):
        create_reservation(
            reservation_repo=reservation_repo,
            space_repo=space_repo,
            id_space=space.id_space,
            start_datetime=start,
            end_datetime=end,
            event_name="Evento",
            client_name="Cliente",
            clien_email="cliente@test.com"
        )