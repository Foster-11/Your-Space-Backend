# Modelo de dominio de YourSpace

Este documento describe los conceptos de negocio actuales. Las clases de
`domain/models/` son dataclasses independientes de SQLAlchemy; los modelos ORM
y las relaciones de persistencia se encuentran en `infrastructure/db/models/`.

## Entidades actuales

- **Owner**: `id_owner`, nombre, apellido, email y contraseña hasheada.
- **Space**: `id_space`, `id_owner`, nombre, capacidad y descripción opcional.
- **Reservation**: `id_reservation`, `id_space`, fechas de inicio/fin, evento,
  datos del cliente, asistentes esperados y descripción opcional.

Las referencias entre objetos se expresan actualmente mediante identificadores:
un `Space` guarda `id_owner` y una `Reservation` guarda `id_space`. Las
cardinalidades previstas son Owner 1:N Space y Space 1:N Reservation.

## Reglas y casos de uso

Los servicios contienen lógica para el registro/login de owners y la creación
de espacios y reservas. Entre las validaciones presentes están la unicidad del
email, la existencia del espacio, el orden de las fechas, la ausencia de
solapamientos y la capacidad del espacio. La cancelación está iniciada, pero
requiere completarse y probarse. Este listado no implica que todos los
endpoints HTTP estén integrados.



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