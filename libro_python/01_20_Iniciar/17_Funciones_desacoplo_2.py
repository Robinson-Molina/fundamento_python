import sys

MIN=0
MAX=100

def pedir_numero(invitacion):
    while True:
        entrada=input(invitacion)
        
        try:
            entrada=int(entrada)
        except:
            print("Solo estan autorizados los caracters [0-9]",file=sys.stderr)
        else:
            return entrada

def pedir_numero_limite(invitacion,minimo=MIN, maximo=MAX):
    while True:
        invitacion = "{} entre {} y {} incluidos >".format(invitacion,minimo,maximo)
        
        entrada= pedir_numero(invitacion)
        invitacion=""
        if minimo <= entrada <=maximo:
            return entrada


def  jugar_una_vez(numero, minimo, maximo):
    intento=pedir_numero_limite("Adivine el numero",minimo, maximo)

    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
        victoria = False
    else:
        print("!Ha Ganado!")
        victoria = True
        minimo = maximo =intento
    return victoria, minimo, maximo

def jugar_una_partida(numero, minimo, maximo):
    victoria=False
    while not victoria:
        victoria, minimo, maximo, =jugar_una_vez(
            numero,
            minimo,
            maximo
            )


def run():
    minimo=maximo=0
    while True:
        minimo=pedir_numero("Seleccione el minimo >")
        maximo=pedir_numero("Selecione el maximo >")

        if maximo>minimo:
            break
    
    numero = pedir_numero_limite("introduzca el numero a adivinar",minimo,maximo)
    while True:
        victoria, minimo, maximo =jugar_una_vez(numero,minimo,maximo)
        if victoria:
            break

if __name__ == '__main__':
    run()