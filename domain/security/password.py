from passlib.context import CryptContext
 
# Contexto de hashing de contraseñas.
# Define qué algoritmo se usa y cómo debe comportarse.
_pwd_context = CryptContext(
    schemes=["bcrypt"],        # bcrypt es un algoritmo seguro para contraseñas
    deprecated="auto"          # permite migrar hashes antiguos si cambia el algoritmo
)
 
 
def hash_password(plain_password: str) -> str:
    """
    Recibe una contraseña en texto plano y retorna su versión hasheada.
    El hash es lo que se almacena en la base de datos, nunca la contraseña real.
    """
    return _pwd_context.hash(plain_password)
 
 
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compara una contraseña en texto plano con un hash almacenado.
   
    - Retorna True si coinciden
    - Retorna False si no coinciden
    """
    return _pwd_context.verify(plain_password, hashed_password)