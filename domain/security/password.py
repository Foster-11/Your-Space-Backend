from passlib.context import CryptContext
 
# Contexto de hashing de contraseñas.
# Define qué algoritmo se usa y cómo debe comportarse.
_pwd_context = CryptContext(
    schemes=["bcrypt_sha256"],        # bcrypt es un algoritmo seguro para contraseñas
    deprecated="auto"          # permite migrar hashes antiguos si cambia el algoritmo
)
 
MAX_BCRYPT_PASSWORD_LENGTH = 72


def hash_password(plain_password: str) -> str:
    """
    Genera un hash seguro a partir de una contraseña en texto plano.

    bcrypt solo procesa los primeros 72 bytes, por lo que truncamos
    explícitamente para evitar errores en tiempo de ejecución.
    """
    safe_password = plain_password[:MAX_BCRYPT_PASSWORD_LENGTH]
    return _pwd_context.hash(safe_password)

 
 

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña coincide con su hash.
    """
    safe_password = plain_password[:MAX_BCRYPT_PASSWORD_LENGTH]
    return _pwd_context.verify(safe_password, hashed_password)

