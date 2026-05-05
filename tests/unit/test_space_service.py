"""
Este test valida:
1. Que se cree correctamente un space asociado a un owner
2. Que el space tenga nombre (regla de negocio)
3. Que el space tenga capacidad definida y válida
4. Que el space esté asociado a un owner existente
"""
 
import uuid
import pytest
 
from domain.models.owner import Owner
from domain.services.space_service import create_space
from domain.repositories.fakes import FakeOwnerRepository, FakeSpaceRepository
 
 
def test_create_space_successfully():
    # Arrange
    # Se preparan todos los datos y dependencias necesarias para el test.
    # Nada se ejecuta aún.
 
    owner_repo = FakeOwnerRepository()
    space_repo = FakeSpaceRepository()
 
    # Se crea un owner con datos "quemados" (fake),
    # que vivirá únicamente en memoria durante el test.
    owner = Owner(
        id_owner=uuid.uuid4(),
        name="Susana",
        last_name="Rios",
        email="susana@test.com",
        password="hashed_password"
    )
 
    owner_repo.add(owner)
 
    # Act 
    # Se ejecuta la acción que se quiere probar.
 
    space = create_space(
        space_repo=space_repo,
        owner_repo=owner_repo,
        id_owner=owner.id_owner,
        name="Sala Meet Gala",
        description="The Main Meet Gala Room",
        capacity=300
    )
 
    # Assert
    # Se verifican los resultados esperados.
 
    # Verifica que la función retornó un objeto y no None.
    assert space is not None
 
    # Verifica que el nombre fue asignado correctamente.
    assert space.name == "Sala Meet Gala"
 
    # Verifica que la capacidad fue asignada correctamente.
    assert space.capacity == 300
 
    # Verifica que el space quedó asociado al owner correcto.
    assert space.id_owner == owner.id_owner