import sys


MAX=99
MIN=0

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

def run():
    minimo=maximo=0
    while True:
        minimo=pedir_numero("Seleccione el minimo >")
        maximo=pedir_numero("Selecione el maximo >")

        if maximo>minimo:
            break
    
    numero = pedir_numero_limite("introduzca el numero a adivinar",minimo,maximo)

if __name__ == '__main__':
    run()

