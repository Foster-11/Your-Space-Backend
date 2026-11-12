# Pytest descubre automáticamente los archivos llamados conftest.py.
# Este archivo añade la raíz del repositorio a sys.path para que los tests
# puedan importar los paquetes del proyecto desde cualquier subdirectorio.

import sys
import os

sys.path.insert(
    0,  # Pone la raíz al inicio de la búsqueda de módulos.
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)