# Infrastructure

La infraestructura contiene los detalles técnicos con los que la aplicación
accede a recursos externos, como la base de datos. En este proyecto, el código
de persistencia está bajo `infrastructure/db/`.

## Modelos de dominio y modelos ORM

Hay dos representaciones distintas de los datos:

- `domain/models/` contiene dataclasses (`Owner`, `Space` y `Reservation`).
  Representan conceptos del negocio y no importan SQLAlchemy.
- `infrastructure/db/models/` contiene las clases ORM de SQLAlchemy, con
  nombres de tabla, columnas, claves foráneas y relaciones. Son detalles de
  persistencia; no son las entidades de `domain/models`.

`infrastructure/db/base.py` define `Base`, una clase declarativa compartida.
SQLAlchemy usa la metadata asociada a esta clase para registrar los modelos ORM.
`Base` no es una entidad ni una tabla. Mantener el archivo en `infrastructure/db/`
es una organización válida: está en la misma capa técnica que la base de datos
y evita que el dominio dependa de SQLAlchemy. También sería válido ubicarlo en
`infrastructure/db/models/base.py` si se prefiere agruparlo con los modelos ORM;
no debe moverse a `domain/models/`.

## Repositorios

Los repositorios SQLAlchemy están en `infrastructure/db/repositories/`. Cada
uno recibe una `Session` y actúa como adaptador de persistencia:

1. Recibe o devuelve un objeto de dominio.
2. Convierte el objeto de dominio en un modelo ORM para guardar o consultar.
3. Ejecuta las operaciones de SQLAlchemy y convierte el resultado ORM de vuelta
   a un objeto de dominio.

Por ejemplo, el servicio de reservas trabaja con `Reservation` del dominio y
usa operaciones como comprobar solapamientos y guardar. El repositorio traduce
esas operaciones a consultas sobre el modelo ORM de reservas. Así, las reglas
de negocio no necesitan conocer tablas, columnas ni sesiones SQLAlchemy.

Los fakes de `domain/repositories/fakes.py` implementan operaciones equivalentes
en memoria para aislar las pruebas unitarias de la base de datos. Los servicios
usan esos métodos por convención (por ejemplo, `add` o `get_space_by_id`), sin
que actualmente exista una interfaz o `Protocol` formal de repositorio.

## Estado actual y siguiente integración

Los modelos ORM y los repositorios están en construcción. La API todavía pasa
`None` como repositorio en varios endpoints, así que los repositorios SQLAlchemy
no forman parte del flujo HTTP ejecutable. Además, `models/__init__.py` exporta
`Owner`, `Space` y `Reservation`, mientras algunos repositorios importan los
nombres `OwnerModel`, `SpaceModel` y `ReservationModel`; esa diferencia debe
resolverse antes de integrar esa capa. También debe acordarse el valor de
`id_state`: es opcional en la dataclass del dominio pero obligatorio en el ORM.

Cuando se conecte la infraestructura, la composición de la aplicación deberá
crear/proveer la sesión y el repositorio concreto al servicio. La dirección de
dependencias deseada es que infraestructura conozca los modelos del dominio y
sus operaciones esperadas, mientras que el dominio no importe modelos ORM,
sesiones ni SQLAlchemy.
