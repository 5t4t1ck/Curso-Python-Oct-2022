
primerNumero = input("Por favor ingrese el primer valor: ")

try:
    primero = int(primerNumero)
except:
    primero = "cadena"

if primero == "cadena":
    print("El valor ingresado no es un entero.")
    exit()

segundoNumero = input("Por favor ingrese el segundo valor: ")

try:
    segundo = int(segundoNumero)
except:
    segundo = "cadena"
#print(primerNumero, segundoNumero)

if segundo == "cadena":
    print("El valor ingresado no es un entero.")
    exit()

simbolo = input("Por favor ingrese la operación que desea realizar: +, -, *, /")

if simbolo == "+":
    print(print("La suma de",primerNumero,"+",segundoNumero,"es: ", primero + segundo))
elif simbolo == "-":
    print(print("La resta de",primerNumero,"-",segundoNumero,"es: ", primero - segundo))

elif simbolo == "*":
    print(print("La multiplicación de",primerNumero,"*",segundoNumero,"es: ", primero * segundo))
elif simbolo == "/":
    print(print("La división de",primerNumero,"/",segundoNumero,"es: ", primero // segundo))