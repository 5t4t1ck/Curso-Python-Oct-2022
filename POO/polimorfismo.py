class Asignatura:

    def enseñar():
        pass

class Matematicas(Asignatura):
    
    def enseñar():
        print("Yo enseño operaciones matemáticas")

class Lenguaje(Asignatura):
    
    def enseñar():
        print("Yo enseño ortografía y gramática")

tema1 = Matematicas
tema1.enseñar()

tema2 = Lenguaje
tema2.enseñar()