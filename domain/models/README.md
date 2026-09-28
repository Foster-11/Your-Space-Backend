### ¿Por qué se utilizan estos imports?

El modelo cumple actualmente dos responsabilidades:

1. Representar una entidad del dominio (`Owner`,  `Reservation` y `Space`).
2. Representar una entidad persistente de SQLAlchemy (modelo ORM).

Por esta razón necesita importar herramientas relacionadas con:

- Identidad (`uuid4`)
- Persistencia en PostgreSQL (`UUID`)
- Definición de columnas y tipos (`sqlalchemy`)
- Relaciones ORM (`sqlalchemy.orm`)
- Registro de modelos ORM (`Base`)

Estos imports permiten que SQLAlchemy pueda convertir la clase, por ejemplo
`Owner` en una representación de la tabla `owner` dentro de la
base de datos.


### Imports:

- uuid4

    Genera identificadores únicos universales (UUID).
    Se utiliza como valor por defecto para la clave primaria
    del Owner.

- UUID

    Tipo de dato específico de PostgreSQL para almacenar UUIDs.
    Permite que id_owner se guarde como UUID nativo en la base
    de datos.

- sqlalchemy as sql

    Alias utilizado para acceder a los componentes principales
    de SQLAlchemy como:
    - Column
    - String
    - Integer
    - ForeignKey
    - etc.

    Ejemplo:
        sql.Column(...)
        sql.String(...)

- sqlalchemy.orm as orm

    Alias utilizado para funcionalidades del ORM relacionadas
    con entidades y relaciones entre modelos.

    Ejemplo:
        orm.relationship(...)

- Base

    Clase base común para todos los modelos ORM del proyecto.

    Heredar de Base permite que SQLAlchemy:
    - registre la entidad como modelo ORM
    - genere metadatos de la tabla
    - gestione relaciones entre entidades
    - cree tablas en la base de datos

    Actualmente Owner, Space y Reservation heredan de Base.
