# domain/exceptions/base.py

"""
Excepción base para TODAS las reglas de negocio del dominio

Este archivo define una jerarquia comun para los errores del negocio,
permitiendo distinguir errores de dominio de errores técnicos

Debe existir este archivo para tener UN PUNTO COMÚN DE CAPTURA DE ERRORES DE NEGOCIO
"""

class DomainError(Exception):
    pass


# Todas las excepciones de dominio deben heredad de DomainError

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