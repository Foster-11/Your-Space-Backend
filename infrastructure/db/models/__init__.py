# Importar todos los modelos para que SQLAlchemy los registre en Base.metadata
from infrastructure.db.models.owner import OwnerInfrastructureModel
from infrastructure.db.models.space import SpaceModel
from infrastructure.db.models.reservation import ReservationModel

__all__ = ["OwnerInfrastructureModel", "SpaceModel", "ReservationModel"]