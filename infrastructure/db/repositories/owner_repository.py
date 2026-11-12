# ../repositories/: se escriben queries, se usan sesiones y se ejecuta sql
# ../repositories/: queries, sesiones y traducción dominio <-> ORM
# Adaptador SQLAlchemy que traduce entre objetos de dominio y modelos ORM.
from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.models.owner import OwnerDomainModel
from infrastructure.db.models import OwnerInfrastructureModel

"""Convierte un modelo ORM de propietario a su representación de dominio."""
def _to_domain(model: OwnerInfrastructureModel) -> OwnerDomainModel:
    return OwnerDomainModel(
        id_owner=model.id_owner,
        name=model.name,
        last_name=model.last_name,
        email=model.email,
        password=model.password, # Por qué? Porque el modelo de dominio también necesita la contraseña para la autenticación y la lógica de negocio relacionada con el propietario.
    )


def _to_model(owner: OwnerDomainModel) -> OwnerInfrastructureModel:
    return OwnerInfrastructureModel(
        id_owner=owner.id_owner,
        name=owner.name,
        last_name=owner.last_name,
        email=owner.email,
        password=owner.password, #Por qué? Porque el modelo de infraestructura también necesita la contraseña para persistirla en la base de datos.
    )


class SqlAlchemyOwnerRepository:
    def __init__(self, session: Session):# Inicializa el repositorio con una sesión de SQLAlchemy
        self.session = session

    """
    Esta clase implementa un repositorio de propietarios utilizando SQLAlchemy.
    """
    def add(self, owner: OwnerDomainModel) -> None:
        self.session.add(_to_model(owner))
        self.session.commit()

    def get_owner_by_id(self, id_owner) -> OwnerDomainModel | None:
        model = self.session.get(OwnerInfrastructureModel, id_owner)
        return _to_domain(model) if model else None

    def get_by_email(self, email: str) -> OwnerDomainModel | None:
        model = self.session.scalar(select(OwnerInfrastructureModel).where(OwnerInfrastructureModel.email == email))
        return _to_domain(model) if model else None

    def delete_owner_by_id(self, id_owner) -> bool:
        model = self.session.get(OwnerInfrastructureModel, id_owner)
        if not model:
            return False
        self.session.delete(model)
        self.session.commit()
        return True