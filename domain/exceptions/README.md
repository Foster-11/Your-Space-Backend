# Excepciones del dominio


Las excepciones de `domain/exceptions/` comunican que una operación no puede
continuar porque se incumplió una regla o no se encontró un recurso esperado.
Por ejemplo:
```
OwnerAlreadyExistsError

InvalidCredentialsError

OwnerNotFoundError
```

Estas excepciones heredan de `DomainError`. Así los servicios pueden describir
problemas del negocio sin depender de HTTP, FastAPI ni de una base de datos. La
capa API decide cómo traducirlas a respuestas HTTP.

Aquí estamos separando los Errores de Dominio vs Errores Técnicos, lo que nos facilitaría mucho trabajo más adelante, aunque construirlo inicialmente resulte engorroso

**Por ejemplo :**

- *Error de dominio:*
```
# Regla de negocio violada
OwnerAlreadyExistsError
```

- *Error Técnico:*
```
# La base de datos está caida
ConnectionRefusedError

# La red falló
TimeoutError

# Problema de persistencia 
SQLAlchemyError
```



# Q&A

**1. ¿Qué son las excepciones?**


**2. ¿Cuales son las buenas prácticas detrás de las excepciones?**