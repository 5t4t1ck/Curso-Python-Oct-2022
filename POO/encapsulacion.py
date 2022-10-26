class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"El precio de venta es: {self.__maxprice}")

    def set_maxprice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.set_maxprice(1000)
c.sell()