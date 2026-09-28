Contenido Próximo:

1. Entidades del dominio
   - Owner
   - Space
   - Reservation

2. Relaciones
   - Owner 1:N Space
   - Space 1:N Reservation

3. Reglas de negocio
   - Email único
   - No solapamientos
   - etc.

4. Casos de uso principales
   - Registrar owner
   - Crear space
   - Crear reserva
   - Cancelar reserva



Sistema de Gestión de Reservas

Arquitectura:
- Monolito Modular
- Dominio Centrado en el Negocio
- Arquitectura por Capas

Dominio Principal:
- Gestión de Espacios
- Gestión de Reservas

Actores:
- Owner

Entidades:
- Owner
- Space
- Reservation