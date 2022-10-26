class Profesion:

    def __init__(self, nombre):
        self.nombre = nombre

    def yoSoyAbuelo(self):
        print("Yo soy Abuelo")

class Profesionales_Salud(Profesion):

    def __init__(self, area):
        pass

    def soyArea(self):
        print("Soy la clase Padre")

class Profesional_Especialidad(Profesionales_Salud):

    def __init__(self, nombre, area, especialidad):
        pass

    def soyespecialidad(self):
        print("Soy la clase nieta")

ortodoncista = Profesional_Especialidad("Juan", "Salud", "Ortodoncia")
ortodoncista.nombre = "Pedro"
print(ortodoncista.nombre)
ortodoncista.yoSoyAbuelo()
ortodoncista.soyArea()
ortodoncista.soyespecialidad()