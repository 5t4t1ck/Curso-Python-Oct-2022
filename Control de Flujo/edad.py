"""
Calcular la edad de una persona
Si es menor de 18 años imprimir "menor a 18 años"
Si es mayor a 18 años imprimir "mayor a 18 años"
Si es mayor a 50 años imprimir "mayor a 50 años"
"""
edad = -5

if edad < 18 and edad > 1:
    print("Es menor de 18")
elif edad > 18 and edad < 50:
    print("Es mayor a 18")
elif edad > 50:
    print("Es mayor a 50")
else:
    print("Ingrese valores natural")

