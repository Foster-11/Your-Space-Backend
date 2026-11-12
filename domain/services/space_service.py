"""Casos de uso para crear espacios y asociarlos con un propietario."""

from os import name

from domain.models.space import SpaceDomainModel # import del modelo de la entidad


def create_space(
        *, # Este asterisco indica que TODOS los parámetros
        # deben pasarse por nombre (keyword-only).
        space_repo, # Provee la operación para guardar el espacio; puede ser fake o SQLAlchemy.

        owner_repo, # Repositorio para validar existencia del owner
        id_owner, 
        name, 
        description, 
        capacity
        ) -> SpaceDomainModel: # Devuelve el objeto de dominio creado.
    
    """
    Crea un nuevo espacio asociado a un propietario existente.

    Reglas de negocio:
    - El propietario debe existir.
    - El nombre no puede estar vacío.
    - La capacidad debe ser mayor que cero.
    """
    # Comprueba la existencia del propietario antes de crear el espacio.
    owner = owner_repo.get_owner_by_id(id_owner)
    if not owner:
        raise ValueError("Owner no existe")
    
    # Rechaza nombres vacíos o compuestos solo por espacios.
    if not name or not name.strip():
        raise ValueError("El nombre del space es obligatorio")

    # Evita guardar espacios sin capacidad utilizable.
    if capacity <= 0:
        raise ValueError("La capacidad debe ser mayor que cero")

    # Construye el objeto de dominio; el repositorio se encarga de persistirlo.
    space = SpaceDomainModel(
        name=name,
        description=description,
        capacity=capacity,
        id_owner=id_owner
    )

    # Solicita al repositorio que guarde el espacio.
    space_repo.add(space)
    return space
