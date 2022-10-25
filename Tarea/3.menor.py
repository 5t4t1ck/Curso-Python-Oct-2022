"""Escriba una función que encuentre el elemento menor de una lista."""

def menor():
    lista = [2,-800, 1000,6,-9,-1000, -200]
    menor = "init"
    for x in lista:
        if menor == "init" or menor > x:
            menor = x
        elif menor < x:
            menor = menor       
    print(menor)

menor()