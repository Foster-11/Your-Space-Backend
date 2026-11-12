# ../repositories/: se escriben queries, se usan sesiones y se ejecuta sql
# ../repositories/: queries, sesiones y traducción dominio <-> ORM
# Adaptador SQLAlchemy que traduce entre objetos de dominio y modelos ORM.
from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.models.space import Space
from infrastructure.db.models import SpaceModel


def _to_domain(model: SpaceModel) -> Space:
    return Space(
        id_space=model.id_space,
        id_owner=model.id_owner,
        name=model.name,
        description=model.description,
        capacity=model.capacity,
    )


def _to_model(space: Space) -> SpaceModel:
    return SpaceModel(
        id_space=space.id_space,
        id_owner=space.id_owner,
        name=space.name,
        description=space.description,
        capacity=space.capacity,
    )


class SqlAlchemySpaceRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, space: Space) -> None:
        self.session.add(_to_model(space))
        self.session.commit()

    def get_space_by_id(self, id_space) -> Space | None:
        model = self.session.get(SpaceModel, id_space)
        return _to_domain(model) if model else None

    def delete_space_by_id(self, id_space) -> bool:
        model = self.session.get(SpaceModel, id_space)
        if not model:
            return False
        self.session.delete(model)
        self.session.commit()
        return True

    def list_all(self) -> list[Space]:
        return [_to_domain(m) for m in self.session.scalars(select(SpaceModel))]