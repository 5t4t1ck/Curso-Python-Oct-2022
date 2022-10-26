class Perro:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} de {self.age} años"

    def ladrar(self):
        print(f"{self.name} ladra fuerte")

perro1 = Perro("Tobby",2)
print(perro1)
perro1.ladrar()