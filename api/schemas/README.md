### ¿Qué son los Schemas?

Los Schemas son contratos de entrada y salida de la API.

Su responsabilidad es:

- Validar datos HTTP de entrada.
- Definir el formato de las respuestas.
- Generar documentación automática de FastAPI.
- Validar tipos, formatos y restricciones básicas antes de invocar los servicios.
- Evitar exponer información sensible.
- Traducir entre el mundo HTTP y el dominio.

Los schemas no sustituyen las reglas de negocio. Por ejemplo, pueden validar
que un campo sea un correo con formato válido o que una capacidad sea positiva;
el servicio/dominio debe validar invariantes que dependan del estado del sistema
o de decisiones propias del negocio.

Las reglas de negocio pertenecen al dominio

Los schemas definen qué datos pueden entrar o salir del sistema y aplican
validación de frontera; no garantizan por sí solos que una operación sea válida
según el estado del dominio.

### ¿Por qué existe este Módulo?
Sin schemas, un cliente podría enviar:
```json
{
  "email": "esto no es un email",
  "password": "1"
}
```
y el router tendría que validar manualmente su formato. Con ***Pydantic***,
FastAPI valida antes de llamar al servicio tipos de datos, formatos, campos
obligatorios y restricciones declaradas en el schema. Las reglas de negocio
siguen siendo responsabilidad del dominio.

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

Es la clase base de todos los schemas. No debe confundirse con el `Base` de
SQLAlchemy, que está en `infrastructure/db/base.py` y sirve para registrar los
modelos ORM. Los schemas heredan de `BaseModel` para usar las funcionalidades
de validación y serialización de Pydantic.

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
Permite ***construir un Schema*** a partir de un ***objeto Python*** cuyos
atributos tengan los mismos nombres. Puede ser un objeto de dominio o un objeto
ORM; en la arquitectura actual, la respuesta de los servicios es un objeto de
dominio y no se debe asumir que el API recibe directamente un modelo SQLAlchemy.

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