# domain/ : Razon de ser del sistema, nucleo del negocio testeable
# ../services/: logica real,  reglas del negocio, toma de decisiones.
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
# 2. Validar email - pending
# 3. hashear contraseña - pending
# 4. validar credenciales - pending
# 5. login : email existe y contraseña coincide - pending

from domain.models.owner import Owner

