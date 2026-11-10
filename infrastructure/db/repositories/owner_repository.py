# ../repositories/: se escriben queries, se usan sesiones y se ejecuta sql
# ../repositories/: queries, sesiones y traducción dominio <-> ORM
from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.models.owner import OwnerDomainModel
from infrastructure.db.models import OwnerInfrastructureModel


def _to_domain(model: OwnerInfrastructureModel) -> OwnerDomainModel:
    return OwnerDomainModel(
        id_owner=model.id_owner,
        name=model.name,
        last_name=model.last_name,
        email=model.email,
        password=model.password,
    )


def _to_model(owner: OwnerModel) -> OwnerModel:
    return OwnerModel(
        id_owner=owner.id_owner,
        name=owner.name,
        last_name=owner.last_name,
        email=owner.email,
        password=owner.password,
    )


class SqlAlchemyOwnerRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, owner: Owner) -> None:
        self.session.add(_to_model(owner))
        self.session.commit()

    def get_owner_by_id(self, id_owner) -> Owner | None:
        model = self.session.get(OwnerModel, id_owner)
        return _to_domain(model) if model else None

    def get_by_email(self, email: str) -> Owner | None:
        model = self.session.scalar(select(OwnerModel).where(OwnerModel.email == email))
        return _to_domain(model) if model else None

    def delete_owner_by_id(self, id_owner) -> bool:
        model = self.session.get(OwnerModel, id_owner)
        if not model:
            return False
        self.session.delete(model)
        self.session.commit()
        return True