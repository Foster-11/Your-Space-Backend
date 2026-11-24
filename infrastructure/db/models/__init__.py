# infrastructure/db/models/__init__.py

# Importar todos los modelos para que SQLAlchemy los registre en Base.metadata y alembic vea las tablas
from infrastructure.db.models.owner import OwnerInfrastructureModel
from infrastructure.db.models.space import SpaceInfrastructureModel
from infrastructure.db.models.reservation import ReservationInfrastructureModel

__all__ = ["OwnerInfrastructureModel", "SpaceInfrastructureModel", "ReservationInfrastructureModel"]