import sys 

numero1=input("Introduzca un primer numero entre 1 y 10: ")
numero2=input("Introdusca un segundo numero entre 1 y 10: ")

try:
    numero1=int(numero1)
    numero2=int(numero2)
except ValueError as e:
    print("La conversión de uno de los números no ha tenido éxito ",file=sys.stderr)
    sys.exit()

# Realizar la comparacion

if 0 < numero1 <11:
    print("El numero 1", numero1, "esta comprendido entre 1 y 10")
else:
    print("El numero 1", numero1, "NO esta comprendido entre 1 y 10")
 
if 0 < numero2 <11:
    print("El numero 2", numero2, "esta comprendido entre 1 y 10")
else:
    print("El numero 2", numero2, "NO esta comprendido entre 1 y 10")