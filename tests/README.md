# YourSpace TESTS

## 📋 Table of Contents

 - [SONARQUBE LOCAL](#sonarqube-local)
  - [Ejecutar pruebas unitarias](#ejecutar-pruebas-unitarias)
  - [Q&A](#Q&A)

## SONARQUBE LOCAL

### 1. Doble click a `StartSonar.bat` dentro de la carpeta `bin` de SonarQube alojado en la ruta que estableciste en tu explorador de archivos

### 2. Log dentro de `http://localhost:9000`  con credenciales de sonarqube, hacer esto ejecutando el archivo `.bat` anteriormente mencionado

### 3. GENERAR EL REPORTE QUE RECIBIRÁ SONARQUBE (hacer esto previamente al paso 4):
 ```bash
 pytest --cov=./ --cov-report=xml
```

### 4. Para ejecutar un Scann:  (ojo, debes tener instalado pysonar) 
 ```bash
pysonar --sonar-token=$SONAR_TOKEN
 ```
**Nota importante:** utilizar el archivo `.env.template`, crear una copia y renombrar como `.env` agregar valor de la variable `SONAR_TOKEN` por el token generado en sonarqube

---
## Ejecutar pruebas unitarias
 ```bash
pytest
 ```


## Q&A
### ¿Qué es SonarQube?
Es una plataforma open source para realizar un análisis estático del código fuente. Evalúa continuamente parámetros cruciales como la duplicación del código, la cobertura de pruebas unitarias o la complejidad ciclomática, aportando métricas precisas que guian las decisiones técnicas. Se enfoca principalmente en identificar y corregir errores, vulnerabilidades de seguridad y puntos críticos en términos de calidad del software.

El proceso de inspección estática genera informes detallados que proporcionan una visioón global sobre aspectos como la calidad técnina, la cobertura de pruebas y la detección temprana de posibles errores críticos.


