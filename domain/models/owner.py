# domain/models/owner.py : entidad de negocio, sin dependencias de persistencia
from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(kw_only=True)
class OwnerDomainModel:
    name: str
    last_name: str
    email: str
    password: str  # Guarda el hash generado por el servicio, nunca la contraseña en texto plano.
    id_owner: UUID = field(default_factory=uuid4)