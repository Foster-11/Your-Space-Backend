# YourSpace TESTS

## Contenido

- [Análisis con SonarQube](#análisis-con-sonarqube)
- [Ejecutar las pruebas](#ejecutar-las-pruebas)
- [TDD y niveles de prueba](#tdd-y-niveles-de-prueba)
- [Preguntas frecuentes](#preguntas-frecuentes)

## Análisis con SonarQube

### 1. Inicia SonarQube

Ejecuta `StartSonar.bat` desde la carpeta `bin` de tu instalación local de
SonarQube.

### 2. Inicia sesión

Abre `http://localhost:9000` e inicia sesión después de que SonarQube arranque.

### 3. Genera el reporte de cobertura

Ejecuta las pruebas con cobertura antes de lanzar el análisis:
 ```bash
 pytest --cov=./ --cov-report=xml
```

### 4. Para ejecutar un scan (requiere tener `pysonar` instalado)

Define `SONAR_TOKEN` en la terminal que ejecutará el scanner. No es necesario
guardar el token en el archivo `.env` de la aplicación.

**Bash:**
 ```bash
export SONAR_TOKEN="<token>"
pysonar --sonar-token="$SONAR_TOKEN"
 ```

**PowerShell:**
 ```powershell
$env:SONAR_TOKEN = "<token>"
pysonar --sonar-token=$env:SONAR_TOKEN
 ```

---
## Ejecutar pruebas unitarias
 ```bash
pytest
 ```

## TDD y niveles de prueba

TDD (desarrollo guiado por pruebas) es un ciclo: escribir una prueba que expresa
un comportamiento, ejecutar la prueba y observar que falla, implementar lo
mínimo necesario y volver a ejecutar las pruebas. Luego se puede mejorar el
código manteniendo las pruebas en verde.

### Pruebas unitarias de servicios

Las pruebas de `domain/services/` usan repositorios fake en memoria. Así
verifican reglas y resultados del servicio sin conectarse a Neon, PostgreSQL o
SQLAlchemy. El fake debe ofrecer las mismas operaciones que el servicio
necesita; los cambios a esas operaciones deben reflejarse también en sus tests.

El servicio no tiene que dejar de usar un repositorio para que la persistencia
real funcione. Debe depender de las operaciones que necesita, no de una
`Session` ni de una clase ORM. En ejecución, se le entrega un repositorio
SQLAlchemy; en una prueba unitaria, uno fake.

### Pruebas de integración

Las pruebas de integración verifican piezas reales conectadas entre sí:

1. Probar un repositorio SQLAlchemy contra una base de pruebas valida consultas,
   conversiones, claves foráneas y restricciones.
2. Probar la API con `TestClient` valida rutas, schemas, códigos HTTP y la
   composición de dependencias.
3. Las pruebas end-to-end recorren la aplicación desde una solicitud externa
   hasta su respuesta y pueden incluir una base de datos de pruebas.

No uses la base de datos con datos reales de Neon como base de pruebas. Usa una
base o rama aislada y limpia los datos entre pruebas; para cambios de esquema,
aplica las mismas migraciones que se usarán en los otros entornos.

Las pruebas unitarias actuales cubren principalmente servicios con fakes. Las
pruebas de repositorios contra una base de datos y la integración HTTP con
persistencia aún deben añadirse.


## Preguntas frecuentes

### ¿Qué es SonarQube?

SonarQube analiza código fuente y reporta problemas de calidad, mantenibilidad
y seguridad. La cobertura indica qué líneas ejecutan las pruebas; por sí sola
no demuestra que el comportamiento sea correcto.

### ¿Qué es testeable en un backend?

### ¿Qué es testeable en un sistema completo?

### ¿Qué son pruebas Unitarias?

### ¿Qué otro tipo de pruebas puedo ejecutar en mi sistema?

### ¿Qué significa probar servicios antes que endpoints y cómo esto se relaciona con los tipos de test?

### ¿Qué buenas practicas se pueden evicenciar en las pruebas aplicadas?

¿FailFast en las pruebas?

### ¿Qué es un `Fake Repository` y por qué es relevante en TDD?

Hay que entender algo muy importante: El objetivo de una prueba unitaria es aislar el comportamiento que quiero validar.

### ¿Qué son pruebas de integración? 

Progresión de pruebas - Etapas:
1. Pruebas Unitarias:
Ejemplo:

Probar servicio
```
register_owner()
```

Usando
```
FakeOwnerRepository
```

2. Pruebas de Integración 

contra endpoints reales

```
TestClient(FastAPI)
```

3. Pruebas de Integración con postgreSQL

4. Pruebas End-to-End

### ¿Qué es una prueba end-to-end?

Comprueba un flujo de usuario a través de varias capas de la aplicación. Suele
ser más lenta y requiere más configuración que una prueba unitaria.