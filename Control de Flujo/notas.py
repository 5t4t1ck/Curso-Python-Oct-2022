"""
Nota de un estudiante.
Si el estudiante obtiene 10, imprimir excelente,
Si esta en un rango entre 9 y 10, imprimir muy bueno
Si es un rango entre 8 y 9, imprimir bueno,
Si es un rango entre 7 y 8, imprimir no tan bueno,
Si es un rango menor a 7, imprimir reprobado
"""
nota = 10.5

if nota == 10:
    print("Excelente")
elif nota >= 9 and nota <= 10:
    print("Muy Bueno")
elif nota >= 8 and nota <= 9:
    print("Bueno")
elif nota >= 7 and nota <= 8:
    print("No tan bueno")
elif nota < 7:
    print("Reprobado")
else:
    print("No es un valor contemplado")

