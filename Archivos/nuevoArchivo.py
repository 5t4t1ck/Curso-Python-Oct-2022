archivo = open("Archivos/nombres.txt", "a")

#archivo = open("nombres.txt", "r")
archivo.write("\nDiego Saavedra")
print(archivo.read())
archivo.close()