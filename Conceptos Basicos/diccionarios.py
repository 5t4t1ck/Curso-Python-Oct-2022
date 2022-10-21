#Ejemplos con Diccionarios

diccionario = {
    "nombre":"Diego",
    "apellido":"Saavedra",
    "edad":34,
    "Ciudad":"Loja",
}
print(type(diccionario))
print(diccionario)

print(diccionario["edad"])
#print("La edad de ", diccionario["nombre"], "es ", diccionario["edad"])

print(diccionario.get("Ciudad"))
diccionario["Ciudad"] = "Quito"
print(diccionario)

print(len(diccionario))

diccionario["altura"]="1.65"
print(diccionario)

diccionario.pop("altura")
print(diccionario)

diccionario.popitem()
print(diccionario)

diccionario.popitem()
print(diccionario)

del diccionario["nombre"]
print(diccionario)
