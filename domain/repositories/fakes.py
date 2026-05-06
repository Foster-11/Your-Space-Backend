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
    
    def get_by_email(self, email):
        for owner in self.owners.values():
            if owner.email == email:
                return owner
        return None

 
 
class FakeSpaceRepository:
    def __init__(self):
        # Inicializa una lista vacía para almacenar spaces en memoria.
        # A diferencia de Owner, aquí no necesitamos búsquedas por id aún.
        self.spaces = {}
 
    def add(self, space):
        # Agrega un objeto Space a la lista de spaces en memoria.
        # Simula una operación de persistencia (guardar en base de datos).
        self.spaces[space.id_space] = space

    
    def get_by_id(self, id_space):
        return self.spaces.get(id_space)


class FakeReservationRepository:
    def __init__(self):
        self.reservations = []
        self.overlapping = False

    def exists_overlap(self, id_space, start, end):
        _=(id_space,start,end)
        return self.overlapping

    def add(self, reservation):
        self.reservations.append(reservation)