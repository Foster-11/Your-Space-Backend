# patron AAA para hacer testing (arrange, act, assert)
# Testear: 
# 1. uvicorn.run sea invocado
# 2. con qué argumentos
# 3. que start() tenga un comportamiento esperado, o sea, llamar a uvicorn.run

#test_main.py
import main
from unittest.mock import patch
import uvicorn

def test_start_calls_uvicorn_run_with_correct_arguments():
    # arrange
    # prepara datos
    with patch.object(uvicorn, "run") as mock_run:# no arranca un servidor real
        # un mock es un objeto simulado que imita el comportamiento real de un componente
        
        # act
        # ejecuta una accion
        main.start()

        # assert
        # verifica resultados
        mock_run.assert_called_once_with(
            "api.app:app",
            host="127.0.0.1",
            port=8070,
            reload=True
        )

         
