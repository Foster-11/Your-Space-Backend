# domain/ : Razon de ser del sistema, nucleo del negocio testeable
# ../services/: logica real,  reglas del negocio, lanzamiento de excepciones (fail fast + graceful handling)
#   inputs:
#       datos primitivos
#       repositorios/sesiones (inyectadas)
#   outputs:
#       entidades
#       errores de dominio


# owner_service.py : reglas para los propietarios en el sistema

# owner_service.py

# Respondabilidades clave:
# 1. Registrar owner - pending
# 2. Validar email para login - pending
# 3. hashear contraseña - pending
# 4. validar credenciales para login - pending
# 5. login : email existe y contraseña coincide - pending

from domain.models.owner import Owner
from domain.exceptions import OwnerAlreadyExistsError, InvalidCredentialsError
from domain.security import hash_password, verify_password

def register_owner(
  *,
  owner_repo,
  name: str,
  last_name: str,
  email: str,
  password: str
) -> Owner:# Qué es? por qué esta funcion es diferente a la de los servicios de las demás entidads?
  existing_owner
  
