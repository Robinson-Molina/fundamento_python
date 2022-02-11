
import random
from re import T
import sys

MIN=0
MAX=100
SI=("s", "si", "y", "yes","1")

IA=True
ayuda=True
n_max=10

def pedir_numero(invitacion):
    while True:
        entrada=input(invitacion)
        
        try:
            entrada=int(entrada)
        except:
            print("Solo estan autorizados los caracters [NUMERICO]",file=sys.stderr)
        else:
            return entrada

def asignar_numero_limite(invitacion,minimo=MIN, maximo=MAX, selecion=False):
    while True:
        if ayuda == True:
            invitacion = "{} entre {} y {} incluidos >".format(invitacion,minimo,maximo)
        else:
            invitacion = "{} >".format(invitacion)

        if selecion == True:
            entrada = pedir_numero(invitacion)
        else:
            entrada = random.randint(minimo,maximo)
        
        invitacion=""
        if minimo <= entrada <=maximo:
            return entrada

def  jugar_una_vez(numero, minimo, maximo):
    
    intento=asignar_numero_limite("Adivine el numero",minimo, maximo,IA)
    if intento < numero and n_max>0:
        print("Demasiado pequeño-->>",intento)
        print("intentos restantes-->>",n_max)
        minimo = intento + 1
        victoria = False
    elif intento > numero and n_max>0:
        print("Demasiado grande-->>", intento)
        print("intentos restantes-->>",n_max)
        maximo = intento - 1
        victoria = False
    elif intento != numero and n_max==0:
        print("!Ha Perdido!")
        victoria = True
        minimo = maximo =intento
    else:
        print("!Ha Ganado!")
        victoria = True
        minimo = maximo =intento
    numero_intentos()
    print("\n")
    return victoria, minimo, maximo

def jugar_una_partida(numero, minimo, maximo):
    victoria=False
    while not victoria:
        victoria, minimo, maximo, =jugar_una_vez(
            numero,
            minimo,
            maximo
            )

def pedir_numero_incognita(minimo, maximo):
    print("Desea ingresar el numero a adivinar??? [SI o NO] > ")
    selecion = input().lower() in SI
    return asignar_numero_limite("Introdusca el numero a adivinar",minimo,maximo,selecion)


def decidir_limite(lvl):
    global n_max
    while True:
        minimo=MIN
        if lvl == 1:
            maximo = 100
            n_max=10
        elif lvl == 2:
            maximo = 1000
            n_max=100
        elif lvl == 3:
            maximo = 1000000
            n_max =1000
        elif lvl == 4:
            n_max=10000
            maximo =1000000000000
        else:
            n_max=10
            lvl=random.randint(1,4)
            maximo=MAX

        if maximo > minimo:
            return minimo, maximo, lvl

def pedir_entrada_si_o_no(invitacion):
    """Por defecto, cualquier respuesta no comtemplada vale NO"""
    try:
        return input(invitacion).lower() in SI
    except:
        return False

def usar_ayuda():
    global ayuda
    valor=pedir_numero("Desea ayuda [0 1]>")
    if valor == 0:
        ayuda=False
        print("Deshabilitado ayuda")
    else:
        ayuda=True
        print("Habilitado ayuda")

def numero_intentos():
    global n_max
    n_max -= 1
    
def usar_AI():
    global IA
    v_IA=pedir_entrada_si_o_no("Deseas jugar con IA  [SI NO]")
    if not v_IA:
        print("Desativado modo IA")
        IA=True
        return
    else:
        IA=False
        print("JAJAJAJAJA A Jugar")


def jugar():
    
    while True:
        lvl=pedir_numero("Seleccione el nivel de 1-4> ")
        minimo, maximo, lvl= decidir_limite(lvl)
        print("Nivel Asignado",lvl)

        usar_ayuda()
        usar_AI()

        numero=pedir_numero_incognita(minimo,maximo)
        jugar_una_partida(numero,minimo,maximo)
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida? >"):
            print("Hasta pronto")
            return


if __name__ == '__main__':
    jugar()