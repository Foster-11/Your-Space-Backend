# domain/ : Razon de ser del sistema, nucleo del negocio testeable
# ../services/: logica real,  reglas del negocio, lanzamiento de excepciones (fail fast + graceful handling)
#   inputs:
#       datos primitivos
#       repositorios/sesiones (inyectadas)
#   outputs:
#       entidades
#       errores de dominio


# owner_service.py : reglas para los propietarios en el sistema - Entidad de identidad

# domain/services/owner_service.py

# Respondabilidades clave:
# 1. Registrar owner - check
# 2. Validar email para login - check
# 3. hashear contraseña - check
# 4. validar credenciales para login - check
# 5. login : email existe y contraseña coincide - check

from domain.models.owner import Owner
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
  owner_repo, # abstraccion del acceso a datos, inyectada para desacoplar el dominio de la BD
  name: str,
  last_name: str,
  email: str,
  password: str
) -> Owner:# typehint - indica qué retorna la función. Mejora legibilidad, test y análisis estático
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
    
    owner = Owner(
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
) -> Owner:
    """
    Valida credenciales y retorna owner autenticado
    """
    owner = owner_repo.get_by_email(email) 


    if not owner or not verify_password(password, owner.password):
     raise InvalidCredentialsError("Email o contraseña inválidos")

    return owner
