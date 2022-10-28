#archivo = open("Archivos/nombres.txt","x")
archivo = open("Archivos/nombres.txt","r")
#print(archivo.read())
#print(archivo.readline())
#print(archivo.readline())
#print(archivo.readline())
#print(archivo.readline())

for x in archivo:
  print(x)

archivo.close()