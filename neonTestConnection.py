# Este archivo tiene el propósito de probar la conexión a la base de datos Neon usando SQLAlchemy y dotenv.
# Para probarlo es muy sencillo: utiliza una terminal donde tengas activo el ambiente virtual
# y ejecuta el archivo con: python neonTestConnection.py
# Asegúrate de tener un archivo .env con la variable NEON_URL configurada correctamente.
# la salida debe ser algo similar a : Neon db version : PostgreSQL 17.11 (9045acd) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14+deb12u1) 12.2.0, 64-bit

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


# Create engine
engine = create_engine(DATABASE_URL)

# Test connection
with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    print("Neon db version :", result.scalar())


