# main.py : Inicia el servidor y define la configuración de ejecución

import uvicorn

# Funcion que inicia el servidor con uvicorn - facilita el testing declarar el inicio del server de esta manera
def start():
    uvicorn.run(
        #Configuración
        "api.app:app",
        host="127.0.0.1",
        port=8070,
        reload=True
    )


"""
Python crea automaticamente una variable llamada __name__ en cada archivo .py
Si al momento de ejecutar un comando para hacer alguna acción de python (en este caso, iniciar el servidor), el valor de __name__ es "__main__", entonces se ejecuta la función start() ya que el resultado de este condicional es True.

Si no existiera esto, si el archivo se importara en otro modulo, la función start() se ejecutaría automáticamente, lo cual no es deseable en la mayoría de los casos. Por eso se utiliza este condicional para asegurarse de que el servidor solo se inicie cuando se ejecute directamente este archivo.
"""
if __name__ == "__main__":  
    start()
