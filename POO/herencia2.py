class Padre:

    def __init__(self, nombre, apellido, profesion):
        self.nombre = nombre
        self.apellido = apellido
        self.profesion = profesion

    def hacerMuebles(self):
        print(f"Yo {self.nombre} puedo hacer muebles")

class Hijo(Padre):

    def __init__(self, nombre, apellido, profesion):
        super().__init__(nombre, apellido, profesion)

    def conducirVehiculo(self):
        print(f"Yo soy {self.nombre}, y puedo conducir vehiculos")

Herman = Padre("Herman", "Suarez", "Carpintero")
print(Herman.nombre)
print(Herman.apellido)
print(Herman.profesion)

Herman.hacerMuebles()

print("-------------------------------------")

Juan = Hijo("Juan", "Suarez", "Conductor")
print(Juan.nombre)
print(Juan.apellido)
print(Juan.profesion)

Juan.hacerMuebles()
Juan.conducirVehiculo()