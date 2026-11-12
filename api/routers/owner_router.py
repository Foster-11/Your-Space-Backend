# routers/ : expone endpoints de cada entidad

# owner_router.py : recibe request, valida datos con shemas y llama al servicio correspondiente

#api/routers/owner_router.py
from fastapi import APIRouter, HTTPException, status

from api.schemas import (
    OwnerCreateSchema,
    OwnerLoginSchema,
    OwnerResponseSchema,
)
from domain.services.owner_service import (
    register_owner,
    login_owner,
)
from domain.exceptions import (
    OwnerAlreadyExistsError,
    InvalidCredentialsError,
)

# Router
router = APIRouter(prefix="/owners", tags=["Owners"])


"""
response_model=OwnerResponseSchema : Indica que la respuesta de este endpoint debe ser un objeto que cumpla con el esquema OwnerResponseSchema. Esto ayuda a FastAPI a validar y documentar la respuesta de la API, asegurando que los clientes reciban datos en el formato esperado.

status_code=status.HTTP_201_CREATED : Indica que se ha creado un nuevo recurso (en este caso, un nuevo propietario) como resultado de la solicitud POST. Esto es útil para que los clientes de la API sepan que su solicitud fue exitosa y que se ha creado un nuevo recurso en el servidor.
"""
@router.post(
    "",
    response_model=OwnerResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_owner(payload: OwnerCreateSchema):
    try:
        owner = register_owner(
            owner_repo=None, # Temporal: debe inyectarse un repositorio para que este endpoint pueda ejecutarse.
            name=payload.name,
            last_name=payload.last_name,
            email=payload.email,
            password=payload.password,
        )
        return owner

    except OwnerAlreadyExistsError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )


@router.post(
    "/login",
    response_model=OwnerResponseSchema,
)
def login(payload: OwnerLoginSchema):
    try:
        owner = login_owner(
            owner_repo=None,  # Temporal: debe inyectarse un repositorio para que este endpoint pueda ejecutarse.
            email=payload.email,
            password=payload.password,
        )
        return owner

    except InvalidCredentialsError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        )
    


@router.get(
    "/{owner_id}", 
    response_model=OwnerResponseSchema
)
def get_owner(owner_id: str):
    # Respuesta de ejemplo; todavía no consulta el repositorio.
    return {
        "id_owner": owner_id,
        "name": "",
        "last_name": "",
        "email": "placeholder@test.com"
    }




@router.get(
    "",
    response_model=list[OwnerResponseSchema],
)
def list_owners():
    return []




@router.delete(
    "/{owner_id}", 
    status_code=204
)
def delete_owner(owner_id: str):
    return None
