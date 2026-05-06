# YourSpace Backend


## 📋 Table of Contents

 - [Description](#Description)

---
## Description

YourSpace is a basic web app for all the events spaces owners. Here, you can manage your spaces. This is the backend of the project, and its created using FastAPI. Let's see step by step how to run it and take considarations

---

## Setup

### Prerequisites

- **Python 3.11.9**
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

### REALIZAR LOS PASOS DEL 2 AL 5 PARA CADA DISPOSITIVO DIFERENTE EN EL QUE CLONÓ EL REPOSITORIO
### Step 2 — Create a virtual environment (just first time)

Las instrucciones para crear un ambiente virtual para implementar FastAPI está en la documentación oficial:
```
https://fastapi.tiangolo.com/virtual-environments/#install-packages-directly
```
#### **Crear entorno virtual**
Asegurese de estar ubicado en el repositorio del proyecto
```bash
python -m venv .venv
```

 - Asegurarse de esto antes de hacer un push!
Iniciar repositorio en git y agregar al .gitignore el archivo .venv
```bash
echo "*" > .venv/.gitignore
```

### Step 3 — Activar el entorno virtual
Hacer esto cada que inicias la terminal para ejecutar tu proyecto
**terminal bash:**
```bash
source .venv/Scripts/activate
```

**terminal powerShell:**
```bash
.venv\Scripts\Activate.ps1
```

### Step 4 — Actualizar a la última version el pip
```bash
python -m pip install --upgrade pip
```

### Step 5 — Instalar los paquetes por medio de requirements.txt
```bash
pip install -r requirements.txt
```



---

## How to run the project

```bash
uvicorn main:start
```



The next URL show the documentation of this project
`http://127.0.0.1:8000/docs`


---
## SONARQUBE LOCAL

### 1. Doble click a StartSonar.bat dentro de la carpeta bin de SonarQube

### 2. Log dentro de `http://localhost:9000`  con credenciales de sonarqube, hacer esto ejecutando el archivo .bat anteriormente mencionado

### 3. GENERAR EL REPORTE QUE RECIBIRÁ SONARQUBE(hacer esto previamente al paso 4):
 ```bash
 pytest --cov=./ --cov-report=xml
```

4. Para ejecutar un Scann:  (ojo, debes tener instalado pysonar) 
 ```bash
pysonar --sonar-token=$SONAR_TOKEN
 ```
**Nota importante:** utilizar el archivo `.env.template`, crear una copia y renombrar como `.env` agregar valor de la variable `SONAR_TOKEN` por el token generado en sonarqube

---
## Ejecutar pruebas unitarias
 ```bash
pytest
 ```

Estructura esperada: 

```

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
├── complements/            # Archivos de documentación complementaria 
│   ├── YourSpace-DbDiagram.dbml
│   ├── instructions.txt
├── domain/                 # Núcleo del negocio (TESTEABLE)
│   ├── exceptions/
│   │   ├── base.py
│   │   └── owner.py
│   ├── models/             # Entidades del negocio
│   │   ├── owner.py
│   │   ├── space.py
│   │   └── reservation.py
│   ├── repositories/      # mock infrastructure para resting
│   │   ├── fakes.py
│   ├── security/
│   │   └── password.py
│   ├── services/           # Lógica del negocio
│   │   ├── owner_service.py
│   │   ├── space_service.py
│   │   └── reservation_service.py
│
├── infrastructure/         # Detalles técnicos
│   ├── db/
│   │   ├── session.py      # conexión Neon/Postgres
│   │   ├── base.py
│   │   └── repositories/
│   │       ├── owner_repository.py
│   │       └── space_repository.py
│   │       └── reservation_repository.py
│   ├── broker/             # futuros eventos/mensajería
│
├── tests/
│   ├── unit/
│   │   ├── test_owner_service.py
│   │   └── test_space_service.py
│   ├── conftest.py        # configuración personalizada para testing - pytest
│
├── requirements.txt
└── README.md


```

Fases del desarrollo del proyecto:
 
1. Definir reglas de negocio 
2. Levantar el servidor (Para nuestro caso, FastApi y uvicorn)
3. Crear modelos y servicios (domain/)
4. Primeros Tests de dominio
5. Implementar lógica mínima   - **Estado actual del repositorio**
6. Creae routers, schemas 
7. Conectar BD, Repositorios, SqlAlchemy
8. Sonarqube **(Implementado localmente)**



# **domain/services/  -> Flujos**

## **Register - api llama a este service :**
1. Recibe name, email, password
2. verifica: si existe email
3. hashea contraseña
4. crea owner
5. devuelve owner

## **Login - api llama a este service**
1. Recibe: email. password
2. busca owner por email
3. valida contraseña
4. si falla - error de dominio
5. si ok - return owner autenticado


Continuación del desarrollo después de domain

# API- Schemas primero  ← AHORA ESTÁS AQUÍ
Dentro de api/:
Definir qué recibe el sistema
Definir qué devuelve
Ocultar detalles del dominio (password, hashes, etc.)
Normalizar nombres, formatos, errores
Ejemplos:
OwnerCreateSchema
OwnerResponseSchema
LoginSchema
SpaceCreateSchema
ReservationCreateSchema

API – Routes (después de schemas)
Una vez los schemas estén claros:
los endpoints son simples
no hay dudas de tipos
el router solo orquesta

Infrastructure (DESPUÉS de API)
Ahora sí:
Repositorios reales (SQLAlchemy)
Session / engine
Inyección de dependencias
Implementar interfaces que hoy tienes fakeadas
Infrastructure implementa lo que API + Domain ya definieron.
Nunca al revés.
