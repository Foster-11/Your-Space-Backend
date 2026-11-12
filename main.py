# main.py : Inicia el servidor y define la configuración de ejecución

import uvicorn

# Encapsula el arranque de Uvicorn para poder probar su configuración sin iniciar el servidor.
def start():
    uvicorn.run(
        # Ruta de importación de la instancia FastAPI.
        "api.app:app",
        host="127.0.0.1",
        port=8070,
        reload=True
    )


"""
Python asigna `__name__` a cada módulo. Al ejecutar este archivo directamente,
su valor es `"__main__"` y se inicia el servidor. Al importar `main` desde otro
módulo, la condición es falsa y el servidor no se inicia automáticamente.
"""
if __name__ == "__main__":  
    start()
