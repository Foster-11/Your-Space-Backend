# main.py : Inicia el servidor y define la configuración de ejecución

import uvicorn

# Funcion que inicia el servidor con uvicorn
def start():
    uvicorn.run(
        #Configuración
        "api.app:app",
        host="127.0.0.1",
        port=8070,
        reload=True
    )

if __name__ == "__main__":  
    start()
