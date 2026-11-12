# Crea el engine de SQLAlchemy usando la URL configurada en el entorno.

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL") # Toma la URL de la base de datos desde las variables de entorno

engine = create_engine(
   DATABASE_URL,
    pool_size=10,              # Máximo de conexiones reutilizables que conserva el pool.
    max_overflow=5,            # Conexiones temporales adicionales cuando el pool está ocupado.
    pool_timeout=30,            # Máximo de segundos de espera por una conexión disponible.
    pool_recycle=1800,          # Reemplaza una conexión al volver a usarla si supera esta antigüedad.
    pool_pre_ping=True,        # Comprueba la conexión al tomarla del pool.
    echo=False                 # Si es True, registra las consultas SQL para depuración.
)