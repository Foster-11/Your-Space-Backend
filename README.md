# 📘 YourSpace Backend
> YourSpace es un laboratorio de ingeniería de software disfrazado de sistema de reservas 

> ⚠️ ¡Documentación bilingüe!

## 📋 Table of Contents

 - [🗒️ Description](#Description)
 - [🏛️ Technologies](#technologies)
 - [⚙️ Setup](#setup)
 - [💡Cómo correr el código](#cómo-correr-el-código)
 - [🧩 Estructura del Backend](#-estructura-del-backend)
 - [🏛️ Arquitectura del Sistema](#️-arquitectura-del-sistema)
 - [🧱 Capas y Módulos](#capas-y-módulos)
 - [❓ Q&A](#qa)
 - [🛤️ Flujos](#️-flujos)

---
## 🗒️ Description

YourSpace is a basic web app for all the events spaces owners. Here you can manage your spaces. This is the -*backend*- project. Let's see step by step how it was built, what you can learn about software engiinering hight level foundations, how to run it and take considarations.


## 🏛️ Technologies and Knowledges

```text
FastAPI
Pytest
Unit tests
Pydantic
Alembic
Arquitectura por capas
SonarQube
Uvicorn
OpenAPI

En progreso ------------------------> Próximo 

LLM Local --> Chatbot
Docker
GitHub Actions
JWT
PostgreSQL
```


## ⚙️ Setup

### Prerequisitos y Tecnologías

*En la máquina local:*
- **Python 3.11.9**
- **pip (last version)**

*Frameworks e imports relevantes:*
- **fastapi** --> web framework
- **psycopg2-binary** --> Database adapter
- **sqlalchemy** --> SQL and ORM features
- **pytest** --> testing framework
- **coverage** --> measuring code coverage
- **pytest-cov** --> pytest plugin
- **passlib** --> hashing password library
- **bcrypt** --> password hashing algorithm

### Paso 1 — Clonar el repositorio

Método HTTPS (el más común) : 

```bash
git clone https://github.com/Foster-11/Your-Space-Backend.git
cd Your-Space-Backend
```

Con SSH (método avanzado): 
```bash
git clone git@github.com:Foster-11/Your-Space-Backend.git
cd Your-Space-Backend
```

### REALIZAR LOS PASOS DEL 2 AL 5 PARA CADA DISPOSITIVO DIFERENTE EN EL QUE CLONÓ EL REPOSITORIO
### Paso 2 — Crear espacio virtual (Solo por 1ra vez)

Las instrucciones para crear un ambiente virtual para implementar FastAPI está en la documentación oficial:
```
https://fastapi.tiangolo.com/virtual-environments/#install-packages-directly
```

Sin embargo, aquí también te indico cómo.
#### **Crear entorno virtual**
Asegurese de estar ubicado en el repositorio del proyecto
```bash
python -m venv .venv
```

 - ***¡Asegurarse de esto antes de hacer un push!***
Iniciar repositorio en git y agregar al `.gitignore` el archivo `.venv`
```bash
echo "*" > .venv/.gitignore
```

### Paso 3 — Activar el entorno virtual
Hacer esto cada que inicias la terminal para ejecutar tu proyecto, *este es un paso muy frecuente.*

**terminal bash:**
```bash
source .venv/Scripts/activate
```

**terminal powerShell:**
```bash
.venv\Scripts\Activate.ps1
```

### Paso 4 — Actualizar a la última version el pip
```bash
python -m pip install --upgrade pip
```

### Paso 5 — Instalar los paquetes por medio de requirements.txt
```bash
pip install -r requirements.txt
```



---

## 💡 Cómo correr el código

```bash
uvicorn main:start
```



En la siguiente url podrás encontrar la documentación generada por FastAPI del proyecto

`http://127.0.0.1:8000/docs`

[Volver arriba](#-table-of-contents)



## 🧩 Estructura del Backend

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
│   └── README.md          # Documentación de las pruebas realizadas
│
├── .env.template
├── .gitignore
├── requirements.txt
├── sonar-project.properties    # Configuración personalizada para sonarQube local
└── README.md


```


## 🏛️ Arquitectura del Sistema

- **¿Qué arquitectura utiliza YourSpace?**

Actualmente, YourSpace está diseñado como un *Monolito Modular* que implementa una *Arquitectura por Capas*.

Esta decisión fue tomada porque el objetivo principal del proyecto es aprender fundamentos sólidos de ingeniería de software antes de abordar arquitecturas más avanzadas como Event Sourcing, CQRS, Microservicios o Multi-Tenancy

- **¿Qué es un Monolito?**

Un monolito es una aplicación donde todos los componentes se despliegan como una sola unidad.

Por ejemplo:
```text
YourSpace
├── API
├── Domain
├── Infrastructure
├── Tests
└── Database
```
En un monolito, todo está dividido internamente en *módulos*  con *responsabilidades definidas*, en lugar de tener todo mezclado, se definen fronteras arquitectónicas. Cada *módulo* interactúa con el otro mediante contratos definidos. Cada *módulo* intenta comportarse como si fuera un sistema independiente. 


Todo forma parte de una única aplicación. Para principiantes como nosotros, es más fácil desarrollar al tener menor complejidad operativa. Sin embargo, a medida que aprendamos más sobre la ingeniería de software, vale la pena completamente desarrollar programas más complejos.

- **Arquitectura por capas**

Consiste en dividir el sistema según responsabilidades, cada capa tiene una función específica dentro de la aplicación:

```text
HTTP Request
      │
      ▼
┌────Module─────┐
│      API      │---> HTTP requests and comunication
└───────┬───────┘
        │
        ▼
┌────Module─────┐
│    Domain     │---> Logical bussines
└───────┬───────┘
        │
        ▼
┌────Module─────┐
│Infrastructure │--->
└───────┬───────┘
        │
        ▼
    PostgreSQL
```




## 🧱 Capas y Módulos


### Domain (Capa)  
Es el corazón y cerebro del backend. Aquí vive el conocimiento del negocio.
**Módulos**
 * **exceptions:**
 * **repositories:**
 * **Models:**
 * **Services:**
 * **security:**

### Api (Capa)
Responsable de exponer funcionalidades mediante HTTP.

**Módulos**
 * **routers:**
 * **schemas:** La responsabilidad de este módulo es definir contratos. Las schemas cumplen 3 funciones críticas: 
 1. Definir el contrato externo del sistema (¿Qué campos recibe el sistema?¿cuáles son obligatorios?¿cuáles son opcionales?¿qué tipo exacto tiene cada campo?¿en qué formato salen los campos?).

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


### Infraestructure (Capa) 
Contiene detalles técnicos. Su responsabilidad es implementar mecanismos concretos para acceder a recursos externos


## ❓Q&A
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

**4. ¿Qué es un release y cómo será abordado en Your-Space?**

**5. ¿Qué es Service Layer y por qué aplica este patrón en YourSpace-Backend?**

**6. ¿Qué será de Your Space en el Futuro?**

Actualmente, bajo las reglas de negocio, your space puede percibirce como un *Monolito Modular*. 
Sin embargo, en el futuro, tiene todo lo necesario para escalar a una arquitectura Multi Tenancy. 

La razón por la que no lo es ahora mismo, es porque el objetivo de este sistema es con fines educativos y prácticos, donde los usarios aprenden los conceptos básicos de la Ingeniería de Software de una manera más simple y digerida.

**7. ¿Qué es el archivo `__init__.py`?**
Es un archivo que se coloca dentro de un paquete para indicar que esa carpeta debe ser tratada como tal.

**8. ¿Qué es FastAPI y qué problema resuelve?**
Es un framework  moderno, su foco diferenciador de muchos otros es que FastAPI se enfoca en crear ***API HTTP*** de una manera sencilla, rápida y estructurada, utilizando las mismas funciones de python en los endpoints y decoradores. Una de las bondades más notorias de FastAPI, es que genera automaticamente la documentación propia de las API's por medio del formato OpenAPI, la cual utiliza la UI de swagger y nos ahorra el uso de herramientas como Postman
---

> ¡¡¡Migrar cada flujo a cada módulo correspondiente!!!

## 🛤️ **Flujos**

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

---
> Esta es una nota temporal para saber en qué parte del backend nos encontramos desarrollando
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



---

Plan - Fases del desarrollo del proyecto:
 
1. Definir reglas de negocio (Paso conceptual)
2. Levantar el servidor (Para nuestro caso, FastApi y uvicorn)
3. Crear modelos y servicios (Empezar desarrolando todo el layer `domain/`)
4. Primeros Tests de dominio (Unit tests)
5. Implementar lógica mínima   - **Estado actual del repositorio**
6. Creae routers, schemas (expandirse al layer `api/`)
7. Sonarqube ***(Implementado localmente)***
8. Conectar BD, Repositorios, SqlAlchemy
