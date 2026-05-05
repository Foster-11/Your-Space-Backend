# python no asume automáticamente el ordel del arbol de carpetas
# por eso hay que decirle cómo hacerlo, así como otro tipo de caracteristicas de las que nos daremos cuenta
# a medida que hagamos tests. 
# Es obligatorio llamar configtest.py a este archivo, ya que de manera automática pytest lee este archivo primero

# en confest.py se puede:
# 1. Configurar entornos de testing
# 2. ajustar sys.path
# 3. definir fixtures globales


# conftest.py

import sys
import os

sys.path.insert(
    0, # Qué siginifica?
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)