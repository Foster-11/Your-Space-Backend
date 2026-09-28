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