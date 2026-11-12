# Q&A

### ¿Qué es una inyección de dependencias y cómo podemos observar esto en el módulo de servicios?

```
# domain/services/owner_service.py
def register_owner(
*,
owner_repo,
...
)
```

# Servicios del dominio

Un servicio del dominio coordina un caso de uso y aplica las reglas que
corresponden a esa operación. Por ejemplo, `register_owner` comprueba si el
email ya está usado, genera un hash para la contraseña, crea el objeto de
dominio y solicita al repositorio que lo guarde.

Los servicios reciben repositorios como dependencias. Así pueden trabajar con
un fake en memoria durante las pruebas unitarias, o con una implementación de
SQLAlchemy cuando la aplicación conecte la persistencia. El servicio no necesita
conocer una `Session`, una tabla ni una clase ORM.

Esta separación no significa que el servicio deba evitar toda interacción con
persistencia: consulta al repositorio y le solicita operaciones. La diferencia
es que el servicio expresa qué necesita el caso de uso, mientras el repositorio
resuelve cómo leer o guardar los datos.

## Flujo de registro

```text
Datos del request ya validados por el schema
    ↓
register_owner(owner_repo=..., datos...)
    ↓
Consulta el email y aplica las reglas del caso de uso
    ↓
Crea un Owner del dominio y lo entrega al repositorio
    ↓
Devuelve el resultado del caso de uso
```

Los tipos de repositorio se usan actualmente por convención y no están
declarados en una interfaz formal. Los fakes permiten probar el servicio, pero
las pruebas de integración siguen siendo necesarias para verificar la
implementación SQLAlchemy. Consulta [la guía de pruebas](../../tests/README.md).
