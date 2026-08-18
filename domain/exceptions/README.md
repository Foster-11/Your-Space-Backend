> Aquí vamos a documentar lo aprendido sobre excepciones


La excepciones en este módulo expresan conceptos del negocio:
```
OwnerAlreadyExistsError

InvalidCredentialsError

OwnerNotFoundError
```

Pensar en las excepciones de esta manera permiten que el **dominio** pueda comunicar qué regla fue violada sin incluir aún : HTTP, FastAPI, etc

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