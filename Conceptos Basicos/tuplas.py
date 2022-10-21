# Ejemplos de tuplas

tuplas = ("Luis", "Pedro", "Maria", "Luis")
print(type(tuplas))
print(tuplas)

print(tuplas.count("Luis"))
print(tuplas.index("Maria"))

print(tuplas[3])

lista = list(tuplas)
print(lista)

lista.append("Juana")
print(lista)

#print(tuple(lista))

rango = range(100)
print(rango)
#numeros = (1,2,3,...,5000)

mylist = list((1,2,3,4))
mytuple = tuple(mylist)
print(mytuple)
print(mylist)
print(type(mylist))
print(type(mytuple))