import os

if os.path.exists("Archivos/Prueba"):
    os.rmdir("Archivos/Prueba")
    print("Directorio eliminado")
else:
    print("El Directorio no existe")
