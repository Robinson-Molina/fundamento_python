def pedir_numero():
    while True:
        entrada = input("Introduzca un número entre 0 y 99: ")
        try:
            entrada = int(entrada)
        except:
            pass
        else:
            if 0 <= entrada <= 99:
                break
    return entrada

print("Introduzca el número a adivinar")
numero=pedir_numero()


print("Intente adivinar el número")
while True: # BUCLE 1
    while True: # BUCLE 2  
        intento = input("Introduzca un número entre 0 y 99: ")
        try:
            intento = int(intento)
        except:
            pass
        else:
            if 0 <= intento <= 99:
                break # Bucle 2
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("¡Ha ganado!")
        break # Bucle 1