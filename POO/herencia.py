class Cuadrilatero:

    def __init__(self, lados):
        self.lados = lados
        self.suma_angulos = 360

    def perimetro(self):
        return sum(self.lados)

class Cuadrado(Cuadrilatero):

    def __init__(self, lados):
        super().__init__(lados)

cuadrilatero_1 = Cuadrado([4,4,4,4])
perimetro_1 = cuadrilatero_1.perimetro()
print(perimetro_1)
print(cuadrilatero_1.suma_angulos)
