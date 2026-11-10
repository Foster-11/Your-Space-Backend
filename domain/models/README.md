# Modelos del dominio

Los modelos en este módulo (`Owner`, `Space` y `Reservation`) son dataclasses
que representan conceptos y datos del negocio. No heredan de SQLAlchemy `Base`,
no declaran tablas y no dependen de la base de datos.

Esta separación permite que los servicios y las pruebas unitarias trabajen con
objetos de dominio sin abrir conexiones ni depender de PostgreSQL. La persistencia
se representa por separado en `infrastructure/db/models/`, donde están las
clases ORM.

Los repositorios de infraestructura realizan la conversión entre ambas
representaciones. Por eso, un modelo de dominio no debe importar ni heredar de
un modelo ORM; que ambos contengan campos equivalentes no los convierte en la
misma clase ni les asigna la misma responsabilidad.
