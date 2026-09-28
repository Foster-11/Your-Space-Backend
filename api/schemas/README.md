### ¿Qué son los Schemas?

Los Schemas son contratos de entrada y salida de la API.

Su responsabilidad es:

- Validar datos HTTP de entrada.
- Definir el formato de las respuestas.
- Generar documentación automática de FastAPI.
- Proteger el dominio de datos inválidos.
- Evitar exponer información sensible.
- Traducir entre el mundo HTTP y el dominio.

Los Schemas no contienen reglas de negocio.

Las reglas de negocio pertenecen al dominio (`domain/services`).

Los Schemas solamente definen qué datos pueden entrar o salir del sistema.

### ¿Por qué existe este Módulo?
Sin schemas, un cliente podría enviar:
```json
{
  "email": "esto no es un email",
  "password": "1"
}
```
y tu servicio tendría que validar todo manualmente. O sea, tendríamos que modificar el código del dominio para hacer estos filtros de validación. Y con ***Pydantic*** es más facil para FastAPI validar automáticamente antes de llegar al dominio: Tipos de datos, formatos, campos obligatorios, restricciones.

```python
class OwnerLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
```

### Explicación de los Imports