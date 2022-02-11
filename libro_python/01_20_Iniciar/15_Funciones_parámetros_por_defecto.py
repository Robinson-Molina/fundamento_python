MIN=0
MAX=99


def pedir_numero(invitacion,minimo=MIN,maximo=MAX):
    # Se completa la invitacion:
    invitacion += " entre " + str(minimo) +" y " + str(maximo) + ":"

    while True:
        entrada=input(invitacion)

        try:
            entrada=int(entrada)
        except:
            pass
        else:
            if minimo <= entrada <= maximo:
                break
    return entrada

def run():
    numero=pedir_numero("Introduzca el numero a adivinar")
    
    minimo=MIN
    maximo=MAX
    while True:
        intento= pedir_numero("Adivine el numero",minimo,maximo)
        if intento < numero:
            print("Demasiado pequeño")
            minimo=intento+1

        elif intento > numero:
            print("Demasiado grande")
            maximo=intento-1
        else:
            print("!Ha Ganado!")
            break

if __name__ == '__main__':
    run()