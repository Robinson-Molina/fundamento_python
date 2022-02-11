import sys

while True:
    # Se entra en un bucle infinito

    #Se pide indroducir un numero
    numero=input("Introduzca un numero entre 1 y 10: ")
    try:
        numero=int(numero)
    except:
        pass
    else:
        # Realizar la comparacion
        if 1<= numero <= 10:
            #tenemos los que queremo, de modo que salimos del bucle
            break

print("Estamos seguros de que", numero, "es un numero y esta comprendido entre 1 y 10 incluidos")