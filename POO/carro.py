class Carro:

    def __init__(self, marca):
        self.marca = marca

    def acelerar(self):
        print("El carro", self.marca, "puede acelerar" )

    def frenar(self):
        print("El carro", self.marca, "puede frenar" )

    def girarAlaDerecha(self):
        print("El carro", self.marca, "puede girar a la derecha")
    
    def girarAlaIzquierda(self):
        print("El carro", self.marca, "puede girar a la izquierda")

carro1 = Carro("Suzuki")
print(carro1.marca)
carro1.acelerar()
carro1.frenar()
carro1.girarAlaDerecha()
carro1.girarAlaIzquierda()

carro2 = Carro("Corsa")
print(carro2.marca)
carro2.acelerar()
carro2.frenar()
carro2.girarAlaDerecha()
carro2.girarAlaIzquierda()