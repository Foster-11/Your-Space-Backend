## **¿Qué es un modelo ORM de SQLAlchemy?**
Cuando definimos: 
```python
class Base(DeclarativeBase):
    pass
```
Se crea una clase *base* común para todas las entidades persistentes. 
- ***¿Qué quiere decir que son entiedades persistentes?***

Es un objeto cuya información puede sobrevivir al cierre de la aplicación

```json
owner = Owner(
    name="Susana",
    email="susana@test.com"
)
```
Supongamos que el objeto anterior existe, Susana actualmente existe almacenada en la RAM. Si el computador se apaga, ese objeto dejará de existir (Susana). En cambio si susana se almacena en la base de datos, exactamente a eso se le llama persistencia. Entonces en este contexto podemos afirmar que Owner, Space y Reservation son entidades persistentes.

Una entidad persistente es un objeto cuya información debe almacenarse de forma permanente en un medio externo (por ejemplo, una base de datos).
Su estado sobrevive a la ejecución de la aplicación y puede recuperarse posteriormente.

Estas entidades heredan de `Base`, permitiendo que SQLAlchemy las registre como modelos ORM y las relacione con tablas de la base de datos.

- ***¿Qué obtiene una entidad al heredar de `Base`?***

Cuando haces
```python
class Owner(Base):
```
SQLAlchemy registra automáticamente esa clase como un modelo ORM. ***Es decir que deja de ser solo una clase Python y se convierte en una representación de una tabla de base de datos***

Para cada clase que herede `Base`, SQLAlchemy termina teniendo una especie de catálogo, que más adelante nos va a permitir ejecutar comandos relacionados con la administración de los datos. 

```
Base
│
├── Owner
├── Space
└── Reservation
```
> Nota que a través de `Base`, vamos centralizando lo que podemos hacer más adelante en la capa de infrastructure

> Las entidades de dominio terminan dependiendo de Infrastructure al existir esta herencia, por lo que podemos concluir que las `entidades de dominio` también son a su vez `entidades ORM`


## Connection Pooling
Esto es un tema muy interesante que descubrí sobre la marcha en la construcción de este repo. Este concepto surge a raiz de un problema.
Primero describamos el problema: En Oracle, SQL Server, PostgreSQL o MySQL cada conexión activa consume memoria de manera persistente y compite por recursos del kernel. Multiplica eso por cientos de microservicios, cada uno con su propio pool, cada uno escalando dinámicamente, cada uno reconectándose ante cualquier fallo transitorio, y obtienes el escenario que llena los foros de soporte: bases de datos que se quedan sin conexiones disponibles, aplicaciones que esperan eternamente, y equipos de infraestructura que reaccionan subiendo el límite de max_connections sin entender que están alimentando al problema, no resolviéndolo.

El connection pooling nació precisamente para evitar ese desperdicio: mantener un conjunto reducido de conexiones físicas reutilizables que las aplicaciones toman, usan y devuelven al pool sin pagar el costo de abrir y cerrar cada vez. Es una idea simple. Su implementación correcta, no tanto


Información tomada de :
```
https://dbaexperts.tech/rendimiento-y-optimizacion/connection-pooling-y-gestion-de-conexiones/
```

Más información útil en :
```
https://stackpractices.com/es/guides/connection-pooling-deep-dive-guide/
```


> Recomiendo hacer las lecturas completas e indagar