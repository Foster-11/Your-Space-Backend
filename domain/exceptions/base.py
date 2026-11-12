# domain/exceptions/base.py

"""
Excepción base para TODAS las reglas de negocio del dominio

Este archivo define una jerarquia comun para los errores del negocio,
permitiendo distinguir errores de dominio de errores técnicos

Debe existir este archivo para tener UN PUNTO COMÚN DE CAPTURA DE ERRORES DE NEGOCIO
La clase común permite capturar errores del dominio sin depender de HTTP ni de
la base de datos.
"""

class DomainError(Exception):
    pass


# Las excepciones que representan errores del negocio heredan de DomainError.

# en proyectos grandes puede incluir:
# 1. Codigos de error
# 2. mensajes estandar
# 3. metadata adicional



"""
Las excepciones expresan reglas del negocio violadas

No representan errores tecnicos

Permiten:
- tests claros
- manejo de API consistente
- desacoplar dominio HTTP
"""