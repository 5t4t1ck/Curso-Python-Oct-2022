"""
def nombreApellido(nombre="", apellido="Saavedra"):
    print("Su nombre es:", nombre)
    print("Su apellido es:", apellido)

#nombreApellido("Diego", "Saavedra")
nombreApellido()"""

"""
def nombreApellido(*nombre):
    print("Su nombre es:", nombre)

nombreApellido("Diego", "Saavedra")"""


"""def nombreApellido(*nombre):
    print("Su nombre es:", nombre[0], nombre[1])

nombreApellido("Diego", "Saavedra")"""

"""def nombreCompleto(nombre, apellido):
    print(nombre, apellido)

nombreCompleto("Saavedra", "Diego")"""

def nombreCompleto(**kwargs):
    print(kwargs["nombre"], kwargs["segundoNombre"], kwargs["apellido"], kwargs["segundoApellido"])

nombreCompleto(nombre="Diego",segundoNombre="Medardo",apellido="Saavedra", segundoApellido="García")