# domain/ : Razon de ser del sistema, nucleo del negocio testeable
# ../services/: logica real,  reglas del negocio, lanzamiento de excepciones (fail fast + graceful handling)
# space_service.py : reglas para los salones en el sistema - Entidad operativa

# space_service.py

# Respondabilidades clave:
# 1. Crear un space asociado a un owner - check
# 2. validar propiedad - ¿?
# 3. reglas de capacidad - check
# 4. listar esapcios - pending
# 5. eliminar un space (nueva regla: no eliminar si tiene reservas futuras a la fecha actual) - pending

from os import name

from domain.models.space import Space # import del modelo de la entidad


def create_space(
        *, # Este asterisco indica que TODOS los parámetros
        # deben pasarse por nombre (keyword-only).
        space_repo, # Es una dependencia inyectada (repository).
        # El service NO sabe cómo se guarda el Space.
        # Solo delega persistencia.

        owner_repo, # Repositorio para validar existencia del owner
        id_owner, 
        name, 
        description, 
        capacity
        ) -> Space: # El service devuelve una instancia de Space
    
    """
    Crea un nuevo Space asociado a un Owner existente.

    Reglas de negocio:
    - El owner debe existir
    - El nombre no puede ser vacío
    - La capacidad debe ser mayor que cero
    """
    #Validar que el owner exista
    owner = owner_repo.get_by_id(id_owner)
    if not owner:
        raise ValueError("Owner no existe")
    
    # Validar nombre
    if not name or not name.strip():
        raise ValueError("El nombre del space es obligatorio")

    # Validar capacidad
    if capacity <= 0:
        raise ValueError("La capacidad debe ser mayor que cero")

    # Crear instancia de Space
    space = Space(
        name=name,
        description=description,
        capacity=capacity,
        id_owner=id_owner
    )

    # Guardar en el repositorio
    space_repo.add(space)
    return space
