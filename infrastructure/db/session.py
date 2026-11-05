# infrastructure/ : Detalles Tecnicos
# ../session.py: conexion con Neon

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
   DATABASE_URL,
    pool_size=10,              # Conexiones mínimas mantenidas
    max_overflow=5,            # Conexiones extra más allá de pool_size
    pool_timeout=30,           # Segundos esperando conexión disponible
    pool_recycle=1800,         # Reciclar conexiones después de 30 minutos
    pool_pre_ping=True,        # Verificar salud de conexión antes de usar
    echo=False
)