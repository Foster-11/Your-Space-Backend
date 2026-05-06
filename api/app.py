
#api/ : capa HTTP. Recibe el trafico HTTP y lo distribuye

# app.py : registra routers y configura middleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import routers


app: FastAPI = FastAPI(
    title="Your Space API",
    version="1.0.0",
    description="API para la gestión de spaces y reservations"
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hola, Susana"}


for router in routers:
    app.include_router(router)
