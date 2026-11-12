# domain/repositories/fakes.py: repositorios en memoria para pruebas unitarias.

"""
Los repositorios fake guardan objetos en memoria y ofrecen las operaciones que
necesitan los servicios. Permiten probar la lógica del servicio sin conectarse a
la base de datos. No sustituyen las pruebas de integración de los repositorios
SQLAlchemy.
"""

#---------OWNER------------------
class FakeOwnerRepository:
    def __init__(self):
        # Constructor de la clase.
        # Se ejecuta automáticamente cuando se crea una instancia del repositorio.
        # Inicializa una estructura en memoria para almacenar owners.
        self.owners = {}
 
    def add(self, owner):
        # Usa el identificador como clave para buscar o reemplazar el registro.
        self.owners[owner.id_owner] = owner
 
    def get_owner_by_id(self, id_owner):
        # Busca un owner en memoria usando su id.
        # Retorna el owner si existe o None si no se encuentra.
        return self.owners.get(id_owner)
    
    def get_by_email(self, email):
        for owner in self.owners.values():
            if owner.email == email:
                return owner
        return None

    def delete_owner_by_id(self, id_owner):
        if id_owner in self.owners:
            del self.owners[id_owner]
 
 #-----------SPACE-----------------
class FakeSpaceRepository:
    def __init__(self):
        # Inicializa un diccionario vacío para almacenar spaces en memoria..
        self.spaces = {}
 
    def add(self, space):
        # Agrega un objeto Space a la lista de spaces en memoria.
        # Simula una operación de persistencia (guardar en base de datos).
        self.spaces[space.id_space] = space

    
    def get_space_by_id(self, id_space):
        return self.spaces.get(id_space)

    def delete_space_by_id(self, id_space):
        if id_space in self.spaces:
            del self.spaces[id_space]
            return True
        return False

    def list_all(self):
        return list(self.spaces.values())

# --------- RESERVATION ---------------
class FakeReservationRepository:
    def __init__(self):
        self.reservations = {}


    def exists_overlap(
    self,
    id_space,
    start_datetime,
    end_datetime,
    ):
        for reservation in self.reservations.values():
            if reservation.id_space != id_space:
                continue

            if (
                start_datetime < reservation.end_datetime
                and end_datetime > reservation.start_datetime
            ):
                return True

        return False
        
    def add(self, reservation):
        self.reservations[reservation.id_reservation] = reservation

    def get_reservation_by_id(self, id_reservation):
        return self.reservations.get(id_reservation)

    def delete_reservation_by_id(self, id_reservation):
        if id_reservation in self.reservations:
            del self.reservations[id_reservation]
            return True
        return False