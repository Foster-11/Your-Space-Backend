"""Casos de uso de propietarios: registro y autenticación."""

from domain.models.owner import OwnerDomainModel
from domain.exceptions import ( # Funciona así gracias a __init__.py
   OwnerAlreadyExistsError, # imports limpios
   InvalidCredentialsError
   )
from domain.security import ( 
   hash_password, 
   verify_password
   )

def register_owner(
  *, # Fuerza el uso de parámetros nombrados
  owner_repo, # Dependencia con operaciones de repositorio; puede ser fake en tests o SQLAlchemy en ejecución.
  name: str,
  last_name: str,
  email: str,
  password: str
) -> OwnerDomainModel:  # Indica el tipo de entidad que devuelve este caso de uso.
    """
    Registra un nuevo owner en el sistema

    Reglas:
    - email unico
    - contraseña hasheada
    """
    existing_owner = owner_repo.get_by_email(email)
    
    if existing_owner:
     raise OwnerAlreadyExistsError("El email ya existe")
    
    hashed_password = hash_password(password) 
    
    owner = OwnerDomainModel(
     name=name,
     last_name=last_name,
     email=email,
     password=hashed_password
    )
      
    owner_repo.add(owner)
    return owner

def login_owner(
      *,
      email: str,
      password: str,
      owner_repo
) -> OwnerDomainModel:
    """
    Valida credenciales y retorna owner autenticado
    """
    owner = owner_repo.get_by_email(email) 


    if not owner or not verify_password(password, owner.password):
     raise InvalidCredentialsError("Email o contraseña inválidos")

    return owner
