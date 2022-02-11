MIN=0
MAX=99

def pedir_numero(invitacion):
    # Se completa la invitacion:
    invitacion += "entre " + str(MIN) +" y " + str(MAX) + ":"

    while True:
        entrada=input(invitacion)

        try:
            entrada=int(entrada)
        except:
            pass
        else:
            if MIN <= entrada <= MAX:
                break
    return entrada

def run():
    numero=pedir_numero("Introduzca el numero a adivinar")

    while True:
        intento= pedir_numero("Adivine el numero")
        if intento < numero:
            print("Demasiado pequeño")
        elif intento > numero:
            print("Demasiado grande")
        else:
            print("!Ha Ganado!")
            break

if __name__ == '__main__':
    run()