# domain/ : Razon de ser del sistema, nucleo del negocio testeable
# ../services/: logica real,  reglas del negocio
# space_service.py : reglas para los salones en el sistema

# space_service.py

# Respondabilidades clave:
# 1. Crear un space asociado a un owner - check
# 2. validar propiedad - ¿?
# 3. reglas de capacidad - check
# 4. listar esapcios - pending
# 5. eliminar un space (nueva regla: no eliminar si tiene reservas futuras a la fecha actual) - pending

from domain.models.space import Space # import del modelo de la entidad


def create_space(
        *, # qué es? qué representa?
        space_repo, # qué es? qué representa?
        id_owner, 
        name, 
        description, 
        capacity
        ):
    
    if capacity <= 0:
        raise ValueError("La capacidad debe ser mayor a 0") # Si el condicional se cumple, qué pasa?
    
    space = Space( # Crea objeto Space??
        name = name,
        description = description,
        capacity = capacity,
        id_owner = id_owner
    )

    space_repo.add(space)
    return space