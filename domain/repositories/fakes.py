# domain/repositories/fakes.py : infraestructura para testing

class FakeOwnerRepository:
    def __init__(self):
        # Constructor de la clase.
        # Se ejecuta automáticamente cuando se crea una instancia del repositorio.
        # Inicializa una estructura en memoria para almacenar owners.
        self.owners = {}
        # Diccionario donde:
        # - la clave será el id del owner
        # - el valor será el objeto Owner completo
 
    def add(self, owner):
        # Agrega un owner al repositorio en memoria.
        # Usamos el id como clave para poder buscarlo rápidamente.
        self.owners[owner.id_owner] = owner
 
    def get_by_id(self, id_owner):
        # Busca un owner en memoria usando su id.
        # Retorna el owner si existe o None si no se encuentra.
        return self.owners.get(id_owner)
 
 
class FakeSpaceRepository:
    def __init__(self):
        # Inicializa una lista vacía para almacenar spaces en memoria.
        # A diferencia de Owner, aquí no necesitamos búsquedas por id aún.
        self.spaces = []
 
    def add(self, space):
        # Agrega un objeto Space a la lista en memoria.
        # Simula una operación de persistencia (guardar en base de datos).
        self.spaces.append(space)