lista = ["Diego", "Saavedra", 34, 88, 1.65, "vivo", "Diego"]
print(type(lista))

print(lista)
lista.append("Quito")
print(lista)
"""lista1 = lista
print(lista1)
lista1.clear()
print(lista1)
print(lista)
print(lista1)"""

lista1 = []
lista1 = lista.copy()
print(lista1)
print(lista.count("Diego"))

print(len(lista1))
lista.append("Diego")
print(len(lista))

vocales = ["a","e","i","o","u"]
print(vocales[1])
print(vocales[3])
print(vocales[4])

print(len(vocales))

vocales.pop()
print(vocales)

vocales.remove("i")
print(vocales)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
numbers.reverse()
print(numbers)

abecedario = ["q","w","e","r","t"]
abecedario.sort()
print(abecedario)

nombres = ["Luis", "Marcos", "Pedro", "Anahi"]
nombres.sort()
print(nombres)

mayusculasMinusculas = ["juan", "Apedro", "Juan", "Pedro"]
mayusculasMinusculas.sort()
print(mayusculasMinusculas)

numbers = [2,6,7,4,9.0,-1,-4, "Diego"]
numbers.sort()
print(numbers)