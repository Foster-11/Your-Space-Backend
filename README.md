# YourSpace Backend


## 📋 Table of Contents

 - [Description](#Description)

---
## Description

YourSpace is a basic web app for all the events spaces owners. Here, you can manage your spaces. This is the backend of the project, and its created using FastAPI. Let's see step by step how to run it and take considarations

---


task : trascript here the "instrucciones.txt" file

---

## Setup

### Prerequisites

- **Python 3.10+**
- **pip**

### Step 1 — Clone the repository

With HTTPS method (the most common) : 

```bash
git clone https://github.com/Foster-11/Your-Space-Backend.git
cd Your-Space-Backend
```

With SSH (an advance method): 
```bash
git clone git@github.com:Foster-11/Your-Space-Backend.git
cd Your-Space-Backend
```

### Step 2 — Create a virtual environment


## How to run the project (Temporarily)

```bash
fastapi dev
```



Use the next URL for enable comunicatin with a frontend repository:
`http://127.0.0.1:8000`

The next URL show the documentation of this project
`http://127.0.0.1:8000/docs`


It's been based on Swagger tool












Estructura: 

root/
├── main.py
│
├── api/                    # Capa HTTP
│   ├── app.py
│   ├── routers/
│   │   ├── owner_router.py
│   │   ├── space_router.py
│   │   └── reservation_router.py
│   ├── schemas/            # Pydantic (request/response)
│   │   ├── owner_schema.py
│   │   └── space_schema.py
│
├── domain/                 # Núcleo del negocio (TESTEABLE)
│   ├── models/             # Entidades del negocio
│   │   ├── owner.py
│   │   ├── space.py
|   |   └── reservation.py
│   ├── services/           # Lógica del negocio
│   │   ├── owner_service.py
│   │   ├── space_service.py
│   |   └── Reservation.py
|
├── infrastructure/         # Detalles técnicos
│   ├── db/
│   │   ├── session.py      # conexión Neon/Postgres
│   │   ├── base.py
│   │   └── repositories/
│   │       ├── owner_repository.py
│   │       └── space_repository.py
│   ├── broker/             # si luego usas eventos
│
├── tests/
│   ├── unit/
│   │   ├── test_owner_service.py
│   │   └── test_space_service.py
│   └── api/
│       └── test_owner_router.py
│
├── requirements.txt
└── pyproject.toml (opcional)




Fases del desarrollo del proyecto:
 
1. Definir reglas de negocio 
2. Levantar el servidor (Para nuestro caso, FastApi y uvicorn)
3. Crear modelos y servicios (Domain/)
4. Primer Test de dominio
5. Implementar lógica mínima
6. Creae routers, schemas 
7. Conectar BD, Repositorios, SqlAlchemy
8. Sonarqube