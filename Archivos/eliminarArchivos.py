import os

if os.path.exists("Archivos/nombres.txt"):
    os.remove("Archivos/nombres.txt")
    print("Archivo eliminado")
else:
    print("El archivo no existe")

#Abacom