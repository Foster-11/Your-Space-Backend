# domain/models/space.py : un salón que pertenece a un owner
from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(kw_only=True)
class SpaceDomainModel:
    id_owner: UUID
    name: str
    capacity: int
    description: str | None = None
    id_space: UUID = field(default_factory=uuid4)