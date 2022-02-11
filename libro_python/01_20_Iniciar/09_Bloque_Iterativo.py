import sys

numero=input("Introduzca un numero entre 1 y 10: ")
try:
    numero=int(numero)
except:
    numero=0

while not 1<= numero <= 10:
    #El numero no es valido
     
    # #Se pide volver a indroducir en numero
    numero= input("Introduzca un numero entre 1 y 10: ")
    try:
        numero=int(numero)
    except:
        numero=0

print("Estamos seguros de que", numero, "es un numero y esta comprendido entre 1 y 10 incluidos")