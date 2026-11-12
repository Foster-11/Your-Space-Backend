# Este archivo tiene el propósito de probar la conexión a la base de datos Neon usando SQLAlchemy y dotenv.
# Para probarlo es muy sencillo: utiliza una terminal donde tengas activo el ambiente virtual
# y ejecuta el archivo con: python neonTestConnection.py
# Asegúrate de tener DATABASE_URL configurada en el entorno o en un archivo .env.
# La salida incluye la versión de PostgreSQL del servidor al que se conectó.

from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Test postgres with Neon Connection
"""
By default, load_dotenv() will:

Look for a .env file in the same directory as the Python script (or higher up the directory tree).
Read each key-value pair and add it to os.environ.
Not override existing environment variables (override=False). Pass override=True to override existing variables.
"""
load_dotenv() # reads variables from a .env file and sets them in os.environ
DATABASE_URL = os.getenv("DATABASE_URL") 


# Crea un engine para abrir conexiones con la base configurada.
engine = create_engine(DATABASE_URL)

# Ejecuta una consulta sencilla para comprobar que la conexión funciona.
with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    print("Neon db version :", result.scalar())

