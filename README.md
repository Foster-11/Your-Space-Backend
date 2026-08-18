# YourSpace Backend


## 📋 Table of Contents

 - [Description](#Description)
 - [Estructura del Backend](#estructura-del-backend)
 - [Setup](#Setup)
 - [How to run the project](#how-to-run-the-project)
 - [Capas y Módulos](#capas-y-módulos)
 - [Q&A](#qa)
 - [Flujos](#flujos)

---
## Description

YourSpace is a basic web app for all the events spaces owners. Here you can manage your spaces. This is the *backend* of the project, and its created using *FastAPI*. Let's see step by step how to run it and take considarations

---

## Estructura del Backend

```

root/
├── main.py
│
├── api/                    # Capa HTTP
│   ├── app.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── owner_router.py
│   │   ├── space_router.py
│   │   └── reservation_router.py
│   ├── schemas/            # Pydantic (request/response)
│   │   ├── __init__.py
│   │   ├── owner_schema.py
│   │   ├── space_schema.py
│   │   └── reservation_schema.py
│
├── complements/            # Archivos de documentación complementaria 
│   ├── YourSpace-DbDiagram.dbml
│   ├── instructions.txt
├── domain/                 # Núcleo del negocio (TESTEABLE)
│   ├── exceptions/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── owner.py
│   │   └── reservation.py
│   ├── models/             # Entidades del negocio
│   │   ├── owner.py
│   │   ├── space.py
│   │   └── reservation.py
│   ├── repositories/      # mock infrastructure para resting
│   │   └── fakes.py
│   ├── security/
│   │   ├── __init__.py
│   │   └── password.py
│   ├── services/           # Lógica del negocio
│   │   ├── __init__.py
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
│   │   ├── test_main.py
│   │   ├── test_owner_service.py
│   │   ├── test_reservation_service.py
│   │   └── test_space_service.py
│   ├── conftest.py        # configuración personalizada para testing - pytest
│
├── .env.template
├── .gitignore
├── requirements.txt
└── README.md


```


## Setup

### Prerequisites and Technologies

*Into your local machine:*
- **Python 3.11.9**
- **pip (last version)**

*Frameworks and relevant imports:*
- **fastapi**
- **psycopg2-binary**
- **sqlalchemy**
- **pytest**
- **coverage** # for sonarqube reports
- **pytest-cov**
- **passlib**
- **bcrypt**

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

Fases del desarrollo del proyecto:
 
1. Definir reglas de negocio 
2. Levantar el servidor (Para nuestro caso, FastApi y uvicorn)
3. Crear modelos y servicios (domain/)
4. Primeros Tests de dominio
5. Implementar lógica mínima   - **Estado actual del repositorio**
6. Creae routers, schemas 
7. Conectar BD, Repositorios, SqlAlchemy
8. Sonarqube **(Implementado localmente)**

---
## Capas y Módulos

**¿Qué es el archivo `__init__.py`?**
Es un archivo que se coloca dentro de un paquete para indicar que esa carpeta debe ser tratada como tal.

**Conceptos Básicos de: módulo, paquete y biblioteca**
- **Módulo :** Cualquier archivo `.py` que contiene código python
- **Paquete :**

### Domain : Es el corazón y cerebro del backend.
**Módulos**
 * **exceptions:**
 * **repositories:**
 * **Models:**
 * **Services:**
 * **security:**

### Api : 
**Módulos**
 * **routers:**
 * **schemas:** La responsabilidad de este módulo es definir contratos. Las schemas cumplen 3 funciones críticas: 1. Definir el contrato externo del sistema (¿Qué campos recibe el sistema?¿cuáles son obligatorios?¿cuáles son opcionales?¿qué tipo exacto tiene cada campo?¿en qué formato salen los campos?).

    Los schemas protegen el dominio. Un ejemplo conceptual teniendo como referencia este repositorio y su contexto de negocio: El dominio tiene un `Owner.pasword` (hash), la api NUNCA expone esa `password`. Esta decisión vive dentro de schemas, no en el dominio

    Traducen entre reglas internas del domain y el mundo exterior (HTTP/Usuario)

    #### Flujo donde encajan los schemas en el sistema

    ```
    HTTP Request
        ↓
    [ Schema (input) ]
        ↓
    [ API Route ]
        ↓
    [ Domain Service ]
        ↓
    [ Domain Model ]
        ↓
    [ API Route ]
        ↓
    [ Schema (output) ]
        ↓
    HTTP Response
    ```

## Q&A
**1. ¿Cómo inicia el servidor?**

La ejecución inicia con `main.py` cuando ejecuta la función que inicia el servidor (`start()`) con uvicorn y esta función dirige al archivo ubicado en `api/app.py`

```
main.py
  ↓
función start()
  ↓
uvicorn.run("api.app:app")
  ↓
FastAPI app vive en app.py
```

LA FUNCIÓN DE `app.py` ES RECIBIR LAS PETICIONES _**HTTP**_ Y DELEGARLAS A LOS MÓDULOS CORRECTOS

`main.py` inicia el servidor y _define las configuraciones de ejecución_


**2. ¿Qué son las configuraciones de ejecución de un servidor? - uvicorn**

ESPACIO PARA RESPUESTA

**3. ¿Cuál es la puerta de entrada HTTP?**

Como se mencionó anteriormente, la puerta de entrada a las solicitudes *HTTP* que envía el usuario desde la interfaz (Frontend), es `app.py` y la función `app()`. Solo participa al inicio y/o al final del flujo, nunca decide "qué hacer" con el negocio

---

## **Flujos**

(Crear mapa de flujo con domain)

### **Domain:**
### **Register - api llama a este service :**
1. Recibe name, email, password
2. verifica: si existe email
3. hashea contraseña
4. crea owner
5. devuelve owner

### **Login - api llama a este service**
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
