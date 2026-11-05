
#api/ : capa HTTP. Recibe el trafico HTTP y lo distribuye

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
CORS: Cross-Origin Resource Sharing. Permite a las aplicaciones web de python gestionar solicitudes de recursos desde dominios diferentes al del servidor.

Middleware: Componente que se ejecuta antes o después de las solicitudes HTTP, permitiendo modificar la solicitud o la respuesta. En este caso, se utiliza para gestionar CORS.
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endpoint raiz, para healthcheck básico : verás este mensaje al acceder a la raíz del API - local: http://127.0.0.1:8070/
@app.get("/")
async def root():
    return "The API is running"


for router in routers:
    app.include_router(router)

"""
Agrupar los routers de esta manera no es necesario si tu aplicación es relativamente pequeña (Podrias escribir todos los endpoints que necesitas en un solo archivo, aquí). Sin embargo, como estamos planificando una arquitectura más modular y escalable, esta práctica facilita la organización y el mantenimiento del código.
"""