- ¿Cuál es la Responsabilidad del Router?

1. Exponer endpoints HTTP.
2. Recibir requests.
3. Utilizar Schemas para validar datos.
4. Invocar servicios del dominio.
5. Traducir excepciones del dominio a respuestas HTTP.
6. Devolver Responses (Schemas).

NO toma decisiones de negocio, su trabajo es *coordinar*.

Esta lista describe la responsabilidad prevista del router. En el estado actual
del código, la integración HTTP está incompleta: varios endpoints de creación
pasan `None` como repositorio, y algunas operaciones de lectura/eliminación
devuelven valores de ejemplo o vacíos. Por eso no debe interpretarse que todos
los endpoints ya consultan o modifican datos persistidos.

Cuando se conecte la infraestructura, la capa de composición/API deberá proveer
una sesión y los repositorios concretos a los servicios. El router no debería
construir consultas SQL ni decidir reglas de negocio.


## Análisis de imports

```python
from fastapi import APIRouter, HTTPException, status
```

- ***APIRouter*** 

Permite agrupar endpoints relacionados, entonces por ejemplo:
```python
router = APIRouter(
    prefix="/owners",
    tags=["Owners"]
)
```
En los documentos que genera FastAPI, los endpoints de `Owner` quedan agrupados:
```text
POST /owners

POST /owners/login

GET /owners

GET /owners/{id}
```

- ***HTTPException***

Permite responder errores HTTP, por ejemplo:
```python
@router.post(
    "",
    response_model=OwnerResponseSchema,
    status_code=status.HTTP_201_CREATED, # USO DE LOS HTTP STATUS CODE
)
def create_owner(payload: OwnerCreateSchema):
    try:
        owner = register_owner(
            owner_repo=None,
            name=payload.name,
            last_name=payload.last_name,
            email=payload.email,
            password=payload.password,
        )
        return owner

    except OwnerAlreadyExistsError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, #USO DE LOS HTTP STATUS CODE
            detail=str(exc),
        )

```

- ***Status***
Este import de FastAPI proviene directamente de `Starlette`. Son un grupo de constantes ya definidas con códigos representados por variables tipo `int`, por ejemplo: `status.HTTP_200_OK` para representar el código HTTP 200

Según la misma documentación de `FastAPI`, los status codes registrados que podemos usar para nuestros desarrollos los puedes encontrar aquí -> [Hypertext Transfer Protocol (HTTP) Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) Y [RFC 9110: STD 97: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)

