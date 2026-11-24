# 📘 YourSpace Backend
> YourSpace es un laboratorio de ingeniería de software disfrazado de sistema de reservas 

> ⚠️ ¡Documentación bilingüe!

## 📋 Table of Contents

 - [🗒️ Description](#️-description)
 - [🏛️ Technologies](#️-technologies-and-knowledges)
 - [⚙️ Setup](#️-setup)
 - [💡Cómo correr el código](#-cómo-correr-el-código)
 - [🧩 Estructura del Backend](#-estructura-del-backend)
 - [🏛️ Arquitectura del Sistema](#️-arquitectura-del-sistema)
 - [🧱 Capas y Módulos](#-capas-y-módulos)
 - [❓ Q&A](#qa)
 - [🛤️ Flujos](#️-flujos)

---
## 🗒️ Description

YourSpace is a basic web app for all the events spaces owners. Here you can manage your spaces. This is the -*backend*- project. Let's see step by step how it was built, what you can learn about software engiinering hight level foundations, how to run it and take considarations.


## 🏛️ Technologies and Knowledges

```text
FastAPI
Pytest
Pydantic
SQLAlchemy
PostgreSQL alojado en Neon (conexión configurada; integración de la API pendiente)
Arquitectura por capas
SonarQube
Uvicorn
OpenAPI

En progreso ------------------------> Próximo 

LLM Local --> Chatbot
Docker
GitHub Actions
JWT
Alembic
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

El repositorio ya debe excluir `.venv` mediante `.gitignore`; no es necesario
añadir el entorno virtual a Git.

### Paso 3 — Activar el entorno virtual
Actívalo en cada terminal que vayas a usar para ejecutar el proyecto.

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

### Configurar la conexión a la base de datos

La aplicación lee `DATABASE_URL` del entorno. Para desarrollo local, se puede
usar un archivo `.env` basado en `.env.template`; no se debe subir el archivo
con credenciales al repositorio. La conexión permite acceder a la base, pero no
crea ni actualiza automáticamente sus tablas. Consulta
[Persistencia e infraestructura](./infrastructure/README.md) para administrar
el esquema con migraciones.

Neon CLI es opcional; no es necesario instalarlo para que SQLAlchemy use una
URL de conexión.

---

## 💡 Cómo correr el código

```bash
python main.py
```

El comando anterior usa la función `start()` de `main.py` y configura Uvicorn
en `127.0.0.1:8070`. También se puede iniciar directamente la aplicación ASGI:

```bash
uvicorn api.app:app --host 127.0.0.1 --port 8070 --reload
```
> Personalmente prefiero ejecutarlo con uvicorn


En la siguiente url podrás encontrar la documentación generada por FastAPI del proyecto

`http://127.0.0.1:8070/docs`

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
│   ├── models/             # Dataclasses del dominio, sin dependencia ORM
│   │   ├── owner.py
│   │   ├── space.py
│   │   └── reservation.py
│   ├── repositories/      # Fakes en memoria para pruebas unitarias
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
│   │   ├── session.py      # configuración del engine SQLAlchemy
│   │   ├── base.py         # Base declarativa de SQLAlchemy
│   │   ├── models/         # Modelos ORM y relaciones
│   │   └── repositories/
│   │       ├── owner_repository.py
│   │       ├── space_repository.py
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

YourSpace está organizado como un monolito con módulos y capas. La separación
está en desarrollo: algunas rutas HTTP aún usan valores de ejemplo y todavía no
están conectadas con los repositorios SQLAlchemy.

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
En un monolito **modular**, los módulos tienen responsabilidades diferenciadas
y se comunican mediante fronteras explícitas. En este repositorio, los servicios
usan operaciones de repositorio por convención; todavía no hay interfaces
formales para esos repositorios. Esta organización puede complementarse con
conceptos de Domain-Driven Design, pero no implica que el sistema implemente
completamente ese enfoque.


Un monolito modular permite desplegar la aplicación como una unidad y mantener
el código organizado en módulos. Esta estructura reduce la complejidad operativa
frente a distribuir el sistema en varios servicios.

- **Arquitectura por capas**

Consiste en dividir el sistema según responsabilidades, cada capa tiene una función específica dentro de la aplicación:

```text
HTTP request
     │
     ▼
API (schemas y routers)
     │
     ▼
Domain (servicios, modelos y comportamiento esperado del repositorio)
     ▲
     │ implementación del acceso a datos
Infrastructure (repositorios SQLAlchemy y modelos ORM)
     │
     ▼
PostgreSQL
```
Para ver la diferencia entre dataclasses, ORM y repositorios, consulta
[la guía de infraestructura](./infrastructure/README.md).

La parte inferior del diagrama describe el diseño buscado, no una integración
completa: algunos routers todavía pasan `None` en lugar de repositorios. Por
eso, los endpoints de creación que dependen de esos servicios aún no pueden
completar el flujo con persistencia.



## 🧱 Capas y Módulos

### Aplication Entry Point

No es una capa como tal. `main.py` y `api/app.py` son los archivos que participan
en el arranque del servidor HTTP.

En `main.py` está el punto de entrada opcional para iniciar Uvicorn, un servidor
ASGI (Asynchronous Server Gateway Interface) que expone la aplicación FastAPI
para recibir tráfico HTTP.

En `api/app.py` se crea la instancia de FastAPI y se registran el middleware y
los routers. FastAPI genera la documentación OpenAPI a partir de las rutas y
schemas declarados.


### Dominio

Contiene modelos que representan datos del negocio, servicios que coordinan
casos de uso, errores de dominio y utilidades de seguridad. Las pruebas
unitarias de servicios usan repositorios fake en memoria.

### API

Expone las funcionalidades mediante HTTP.

**Módulos**
 * **routers:** reciben solicitudes, invocan servicios y traducen resultados o errores a respuestas HTTP.
 * **schemas:** definen los contratos de entrada y salida. Indican qué campos se reciben, cuáles son obligatorios, qué formato deben tener y qué datos se exponen.

    Los schemas controlan qué campos se reciben o se exponen. Por ejemplo,
    `OwnerResponseSchema` no incluye la contraseña. La aplicación debe seguir
    almacenando únicamente la contraseña hasheada, y el servicio es responsable
    de aplicar las reglas del dominio.

    Los schemas traducen entre el formato HTTP y los objetos que usa la
    aplicación. Sus validaciones de tipos y formatos no sustituyen las reglas
    de negocio.

    #### Flujo previsto para una solicitud y su respuesta

    ```
    HTTP Request
        ↓
    [ Schema (input) ]
        ↓
    [ API Route / serialización ]
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


### Infraestructura

Contiene detalles técnicos. En `infrastructure/db/` están el engine y la sesión
SQLAlchemy, los modelos ORM y los repositorios que implementan la persistencia.
Los repositorios traducen entre objetos de dominio y objetos ORM. La API aún no
inyecta estos repositorios de forma consistente; consulta
[Persistencia e infraestructura](./infrastructure/README.md) para más detalles.


## ❓Q&A
**1. ¿Cómo inicia el servidor?**

Al ejecutar `python main.py`, se llama a `start()` y Uvicorn importa la instancia
FastAPI `app` desde `api/app.py`.

```
main.py
  ↓
función start()
  ↓
uvicorn.run("api.app:app")
  ↓
FastAPI app vive en app.py
```

**2. ¿Qué configura Uvicorn?**

Uvicorn es el servidor ASGI que ejecuta la aplicación. En `main.py`, `host`
define en qué interfaz de red escucha, `port` define el puerto y `reload=True`
reinicia el servidor cuando detecta cambios durante el desarrollo. La recarga
automática no está pensada para producción.

**3. ¿Dónde entra una solicitud HTTP?**

La instancia `app` de `api/app.py` es la entrada ASGI de las solicitudes HTTP y
registra middleware y routers. Los routers coordinan cada endpoint; los
servicios del dominio aplican las reglas de negocio.

**4. ¿Qué es un servicio de dominio?**

Un servicio coordina un caso de uso y aplica reglas que pueden requerir
consultar repositorios. Por ejemplo, `create_reservation` comprueba el intervalo,
busca el espacio, valida solapamientos y asistentes, y solicita guardar la
reserva. El servicio recibe el repositorio como dependencia, de modo que sus
pruebas unitarias pueden usar un fake en vez de conectarse a una base de datos.

**5. ¿Qué hace `__init__.py`?**
En este proyecto, marca paquetes de Python y también permite exponer nombres
para imports más sencillos. Python también admite paquetes de espacio de nombres
sin ese archivo, por lo que su presencia no es una regla universal.

**6. ¿Qué es FastAPI?**
Es un framework de Python para construir APIs HTTP. Usa tipos y decoradores
para declarar rutas y genera un esquema OpenAPI que puede mostrarse, por
ejemplo, en Swagger UI. Esta interfaz ayuda a explorar la API; no reemplaza
herramientas de pruebas como Postman.

**7. ¿Qué quiere decir que " los servicios usan operaciones de repositorio por convención"?

Significa que los servicios asumen que el repositorio tendrá ciertos métodos, aunque todavía no existe una interfaz o contrato formal que los obligue.

---

## Flujos de casos de uso

Los siguientes pasos describen el comportamiento previsto en los servicios; no
significan que todos los endpoints estén conectados a la base de datos.

### Registro de propietario

1. El schema de entrada valida los tipos y formatos del request.
2. El router llama al servicio con los datos y un repositorio.
3. El servicio comprueba si el email ya existe, genera el hash de contraseña,
   crea el objeto de dominio y pide al repositorio que lo guarde.
4. El schema de respuesta selecciona los campos que se devuelven; no incluye la
   contraseña ni el hash.

### Inicio de sesión

1. El schema valida la forma de las credenciales.
2. El servicio busca el propietario por email y compara la contraseña con el
   hash guardado.
3. Si las credenciales no son válidas, el servicio comunica un error de dominio;
   el router lo convierte en una respuesta HTTP.


## Estado del desarrollo

El repositorio contiene schemas, routers, servicios, modelos de dominio, fakes
para pruebas unitarias y adaptadores SQLAlchemy en desarrollo. La API aún no
inyecta repositorios reales de forma consistente. Las pruebas actuales se
centran en servicios con fakes; las pruebas de integración con una base de datos
y las migraciones versionadas aún deben incorporarse. Consulta
[la guía de pruebas](./tests/README.md) y
[la guía de persistencia](./infrastructure/README.md) para conocer el propósito
de cada etapa.
