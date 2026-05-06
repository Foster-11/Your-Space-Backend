# routers/ : expone endpoints de cada entidad

# space_router.py : recibe request, valida datos con shemas y llama al servicio correspondiente

from fastapi import APIRouter, HTTPException, status

from api.schemas import (
    SpaceCreateSchema,
    SpaceResponseSchema,
)
from domain.services.space_service import create_space

router = APIRouter(prefix="/spaces", tags=["Spaces"])


@router.post(
    "",
    response_model=SpaceResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_space_endpoint(payload: SpaceCreateSchema):
    try:
        space = create_space(
            space_repo=None,   # infrastructure luego
            owner_repo=None,   # infrastructure luego
            id_owner=payload.id_owner,
            name=payload.name,
            description=payload.description,
            capacity=payload.capacity,
        )
        return space

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )
    

@router.get("/{space_id}", response_model=SpaceResponseSchema)
def get_space(space_id: str):
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.get("", response_model=list[SpaceResponseSchema])
def list_spaces():
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.delete("/{space_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_space(space_id: str):
    raise HTTPException(status_code=501, detail="Not implemented yet")

