
# api/: capa HTTP. Recibe solicitudes y respuestas HTTP.

# app.py : registra routers y configura middleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import routers

# Aquí se crea la aplicación web
app: FastAPI = FastAPI(
    title="Your Space API",
    version="1.0.0",
    description="Your Space API"
)

# esto debe cambiar en producción/otros ambientes para restringir los orígenes permitidos
origins = ["*"]

"""
CORS (Cross-Origin Resource Sharing) es una política del navegador que controla
si una página web puede hacer solicitudes a un servidor de otro origen. Un
origen combina esquema, host y puerto.

Middleware: componente que procesa solicitudes o respuestas durante su paso por
la aplicación. En este caso, el middleware aplica la configuración CORS.
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raíz para comprobar que la aplicación responde.
@app.get("/")
async def root():
    return "The API is running"


for router in routers:
    app.include_router(router)

"""
Cada router agrupa endpoints relacionados. Incluirlos aquí mantiene la
configuración de la aplicación separada de las rutas y facilita localizar y
mantener cada grupo.
"""