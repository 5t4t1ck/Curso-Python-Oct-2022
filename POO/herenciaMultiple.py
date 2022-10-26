class Padre:

    def __init__(self, nombre, habilidad):
        self.nombre = nombre
        self.habilidad = habilidad

    def yoPuedoHacer(self):
        print(f"Yo puedo hacer {self.habilidad}")

class Madre:

    def __init__(self, nombre, habilidad):
        self.nombre = nombre
        self.habilidad = habilidad

    def yoPuedoHacerAlgo(self):
        print(f"Yo puedo hacer {self.habilidad}")

class Hijo(Madre, Padre):

    def __init__(self, nombre, habilidad):
        super().__init__(nombre, habilidad)

    def yoSoloPuedo(self):
        print(f"Yo solo puedo {self.habilidad}")

Pablo = Hijo("Pablo", "correr")
print(Pablo.habilidad)
Pablo.habilidad = "dormir"
print(Pablo.habilidad)
print(Pablo.nombre)
Pablo.nombre = "Juan"
print(Pablo.nombre)

Pablo.yoPuedoHacer()
Pablo.yoPuedoHacerAlgo()
Pablo.yoSoloPuedo()
