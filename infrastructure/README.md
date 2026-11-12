# Persistencia e infraestructura

La infraestructura conecta la aplicación con recursos técnicos externos. En
este proyecto, `infrastructure/db/` contiene la configuración de SQLAlchemy, los
modelos ORM y los repositorios que consultan o modifican la base de datos.

## Tres representaciones, tres responsabilidades

- **Schema de API:** describe los datos que una solicitud puede enviar o que
  una respuesta puede mostrar. Por ejemplo, la solicitud para crear un
  propietario recibe una contraseña sin procesar; la respuesta no la expone.
- **Modelo de dominio:** representa información y conceptos que usan las reglas
  del negocio. Los servicios trabajan con estos objetos, no con tablas.
- **Modelo ORM:** describe cómo se guardan esos datos en tablas con SQLAlchemy:
  columnas, claves primarias y foráneas, restricciones y relaciones.

No es necesario que las tres representaciones tengan los mismos campos. Cada
una debe incluir lo necesario para su responsabilidad y conservar el significado
de los datos cuando la aplicación los transforma.

`infrastructure/db/base.py` define la clase declarativa `Base`. SQLAlchemy usa
su metadata para registrar los modelos ORM. `Base` no es una entidad del negocio
ni crea o actualiza por sí sola las tablas de una base de datos.

## Repositorios y conversión

Un repositorio adapta las operaciones que necesita un servicio a consultas de
persistencia. Por ejemplo, el servicio de reservas solicita comprobar si hay
solapamiento y guardar una reserva. El repositorio SQLAlchemy consulta el modelo
ORM, ejecuta las operaciones con una `Session` y convierte los resultados ORM
en objetos de dominio.

Los repositorios fake de `domain/repositories/fakes.py` realizan operaciones
similares en memoria. Sirven para probar el comportamiento de los servicios sin
una base de datos; no reemplazan las pruebas de integración del repositorio real.
Actualmente, los servicios usan operaciones de repositorio por convención; aún
no hay un `Protocol` o una interfaz formal que las declare.

SQLAlchemy ofrece expresiones para construir consultas sin concatenar cadenas
SQL manualmente. Por ejemplo, `select(...)` representa una consulta que
SQLAlchemy compila al dialecto de la base de datos configurada. Esto no limita
el uso de consultas complejas: pueden expresarse con las herramientas de
SQLAlchemy cuando el caso lo requiera.

## Cómo crear y cambiar las tablas

Las clases ORM describen el mapeo esperado por la aplicación, pero no actualizan
automáticamente un esquema existente. Para administrar cambios de esquema de
forma repetible, se recomienda usar **Alembic**:

1. Cambiar los modelos ORM.
2. Generar y revisar una migración.
3. Aplicar esa migración al entorno de desarrollo o despliegue.

Una migración es un cambio versionado de la estructura de la base de datos.
Permite aplicar los mismos cambios en distintos entornos y deja un historial de
cómo evolucionaron las tablas.

`Base.metadata.create_all()` puede ser útil para preparar una base vacía en una
prueba o prototipo, pero solo crea las tablas que faltan. No modifica tablas
existentes ni sustituye las migraciones. No se recomienda usarlo al arrancar la
aplicación para gestionar el esquema de Neon o de producción.

## Pruebas y transacciones

Las pruebas unitarias de servicios deben usar repositorios fake. Las pruebas de
integración deben verificar que los repositorios SQLAlchemy traduzcan y
persistan correctamente los datos, usando una base de pruebas separada de los
datos reales.

En el código actual, los métodos de escritura de los repositorios llaman a
`commit()`. Esto confirma cada operación desde el repositorio y es sencillo para
un primer ejemplo, pero dificulta agrupar varias escrituras en una transacción.
Al crecer el flujo, conviene decidir el límite transaccional del caso de uso y
confirmar o revertir la sesión desde una unidad de trabajo o desde la capa que
coordina la operación.

## Estado actual

El engine SQLAlchemy toma `DATABASE_URL` del entorno y los modelos ORM y
repositorios están en desarrollo. Los routers aún pasan `None` como repositorio
en algunos casos, por lo que la persistencia no está conectada al flujo HTTP.
También hay que alinear algunos nombres de las clases ORM con las referencias
que usan las relaciones y los repositorios antes de ejecutar esa integración.
