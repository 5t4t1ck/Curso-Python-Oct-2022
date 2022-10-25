class Persona:

    def __init__(self, nombre, apellido, edad, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula

    def presentarse(self):
        print("Mi nombre es", self.nombre, self.apellido, 
            "mi edad es", self.edad, 
            "mi cedula es", self.cedula)

persona1 = Persona("Juan", "Martinez", 34, "1173625162")
persona1.presentarse()

persona2 = Persona("Maria", "Quiñonez", 18, "4356625162")
persona2.presentarse()