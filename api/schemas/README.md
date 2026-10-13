### ¿Qué son los Schemas?

Los Schemas son contratos de entrada y salida de la API.

Su responsabilidad es:

- Validar datos HTTP de entrada.
- Definir el formato de las respuestas.
- Generar documentación automática de FastAPI.
- Proteger el dominio de datos inválidos.
- Evitar exponer información sensible.
- Traducir entre el mundo HTTP y el dominio.

Los Schemas no contienen reglas de negocio.

Las reglas de negocio pertenecen al dominio

Los Schemas solamente definen qué datos pueden entrar o salir del sistema.

### ¿Por qué existe este Módulo?
Sin schemas, un cliente podría enviar:
```json
{
  "email": "esto no es un email",
  "password": "1"
}
```
y tu servicio tendría que validar todo manualmente. O sea, tendríamos que modificar el código del dominio para hacer estos filtros de validación. Y con ***Pydantic*** es más facil para FastAPI validar automáticamente antes de llegar al dominio: Tipos de datos, formatos, campos obligatorios, restricciones.

```python
class OwnerLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
```

### Explicación de los Imports

1. UUID

```python
from uuid import UUID
```
Se utiliza para los campos que tienen un identificador uníco de tipo UUID rn un schema.

2. Datetime
```python
from datetime import datetime
```



3. Pydantic
```python
from pydantic import BaseModel, EmailStr, Field
```
 - ***¿Qué es pydantic?***

Aquí vale completamente la pena explicar *Pydantic*, es una biblioteca de `Python` utilizada para **definir modelos de datos** utilizando [**`type hints`**](#type-hints).
Estos modelos permiten validar la información que entra al sistema antes de que llegue a las reglas del negocio, en otras palabras, pydantic ayuda a definir las reglas de validación de las API's

- ***BaseModel***

Es la clase base de todos los schemas, ocurre algo similar al `Base` de los modelos ORM que vimos en `domain/models`. Los modelos en Schemas heredan de `BaseModel`, de esta clase los diferentes schemas van a poder ajustar su comportamiento gracias a las diferentes funcionalidades de `BaseModel`, según sus necesidades. 

```text 
BaseModel
│
├── Owner_schema
├── Space_schema
└── Reservation_schema
```
- ***EmailStr***

Este es el tipo  especializado en correos electrónicos, aquí pydantic valida automáticamente que el valor recibido tenga formato válido de email

- ***Field***
Permite agregar restricciones y metadatos a los campos

### Request y Response
Basicamente nos referimos a las clases que procesan lo que recibe el sistema backend desde el exterior y lo que responde - Request/Response. Entonces, por ejemplo, en un request, el Schema está diciendo que si quieres crear un `Owner`, el sistema debe recibir exactamente estos datos. Así se definen los contratos HTTP. Aquí definimos qué puede ver el mundo esterior.

### Configuración especial en los Schemas
```python
class Config:
    from_attributes = True
```
Permite ***contruir un Schema*** a partir de un ***objeto python*** cuyos atributos tengan los mismos nombres, por ejemplo:

```python
# Objeto python

owner = owner(...)
```` 

Se transforma en 
```python
OwnerResponseSchema
```
>Nota que en los archivos .py de los schemas, en la respectiva clase del modelo Schema está la clase de config, por eso es posible

### Diagnosticar lo que hace el sistema analizando los schemas de cualquier Backend
Esto es algo que aprendí aquí en este laboratorio, indagando y creando. Podemos saber los limites del sistema, y algunos aspectos detallados de él solo observando lo que hay aquí, puede que en repositorios más complejos y con arquitecturas y patrones diferentes hagan que sea más dificl identificarle.

Ten en cuenta que hay muchos otros componentes que nos van a ayudar a formar un conocimiento más profundo, sin embargo, para una primera fase de contextualización a un sistema que ya existe, analizar este módulo de la capa `api` puede ayudarnos con entender una parte importante del sistema, lo que hace y lo que **NO HACE**.


## Q&A
- ***¿Qué es un Payload? Vemos esto en las funciones de los router llamando schemas***

## Glosario

#### Type Hints:
Permiten indicar de manera explícita los tipos de datos esperados en funciones, variables y estructuras. Aunque Python sigue siendo un lenguaje de programación dinámico, las anotaciones de tipo facilitan el análisis estático del código y mejoran su legibilidad.