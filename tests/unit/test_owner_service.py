import pytest
import uuid

from domain.models.owner import Owner
from domain.services.owner_service import register_owner, login_owner
from domain.exceptions import OwnerAlreadyExistsError, InvalidCredentialsError
from domain.repositories.fakes import FakeOwnerRepository

# test 1: Registro exitoso de un owner

"""
 Este test valida:
 1. Que se registre correctamente un owner con datos válidos
 2. Que el owner registrado tenga un email único (regla de negocio)
"""

def test_register_owner_successfully():
    owner_repo = FakeOwnerRepository()

    owner = register_owner(
        owner_repo=owner_repo,
        name="Susana",
        last_name="Rios",
        email="susana@test.com",
        password="plain_password"
    )

    assert owner is not None
    assert owner.email == "susana@test.com"


# test 2: Registro de un owner con email ya existente
def test_register_owner_email_already_exists():
    owner_repo = FakeOwnerRepository()

    owner_repo.add(
        Owner(
            id_owner=uuid.uuid4(),
            name="Susana",
            last_name="Rios",
            email="susana@test.com",
            password="hashed"
        )
    )

    with pytest.raises(OwnerAlreadyExistsError):
        register_owner(
            owner_repo=owner_repo,
            name="Otra",
            last_name="Persona",
            email="susana@test.com",
            password="password123"
        )


#test 3: Login exitoso de un owner
def test_login_owner_successfully():
    owner_repo = FakeOwnerRepository()

    owner = register_owner(
        owner_repo=owner_repo,
        name="Susana",
        last_name="Rios",
        email="susana@test.com",
        password="password123"
    )

    logged_owner = login_owner(
        owner_repo=owner_repo,
        email="susana@test.com",
        password="password123"
    )

    assert logged_owner.id_owner == owner.id_owner

# test 4: Login con credenciales inválidas
def test_login_owner_invalid_credentials():
    owner_repo = FakeOwnerRepository()

    register_owner(
        owner_repo=owner_repo,
        name="Susana",
        last_name="Rios",
        email="susana@test.com",
        password="password123"
    )

    with pytest.raises(InvalidCredentialsError):
        login_owner(
            owner_repo=owner_repo,
            email="susana@test.com",
            password="wrong_password"
        )