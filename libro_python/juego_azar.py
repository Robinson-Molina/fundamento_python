


import random


cartas_corazon = {x-127137 : chr(x) for x in range(0x1f0a1, 0x1f0ae)}
cartas_picas = {x-127137+13 : chr(x) for x in range(0x1f0a1, 0x1f0ae)}
cartas_diamante = {x-127137+26 : chr(x) for x in range(0x1f0a1, 0x1f0ae)}
cartas_trebol = {x-127137+39 : chr(x) for x in range(0x1f0a1, 0x1f0ae)}
l=[i for i in range(52)]


def Merge(dict1, dict2, dict3, dict4):
    """concatenar las barajas"""
    d= {**dict1,**dict2,**dict3,**dict4}
    return d

def ran(num):
    for i in range(num):
        yield i 

def selec_carta(n):
    
    valor= random.randint(0, n-1)
    #print("este es el valor :" , valor)

    carta_valor=l[valor]
    #print ("este el numero de la lista", l[valor])
    #print ("este la long de la lista", len(l))
    del l[valor]

    selec = juego_baraja[carta_valor]
    del juego_baraja[carta_valor]
    n -= 1
    return n, carta_valor

def mano(c):
    #print("antes",c)
    if c <= 12:
        c = c
    elif 13 <= c <=25 :
        c = c-13
    elif 25 < c < 39 :
        c = c-26
    elif 39 <= c <= 51 :
        c = c-39
    else:
        c = c -41
    
    #  Condicion del juego
    if (c == 10  or c == 11 or  c == 12):
        c=10
    else:
        c=c+1

    if(c == 1):
        c=0

    #print("despues",c)
    return c

def jugador (n):
    
    n, c1= selec_carta(n)
    n, c2= selec_carta(n)
    print(baraja[c1])
    print(baraja[c2])
    
    c1=mano(c1)
    c2=mano(c2)

    #print(c1)
    #print(c2)
    return n,c1,c2

def mesa (n):
    
    n, c1= selec_carta(n)
    n, c2= selec_carta(n)
    print(baraja[c1])
    print(chr(40962))
    
    c1=mano(c1)
    c2=mano(c2)

    #print(c1)
    #print(c2)
    return n,c1,c2

def primera_mano(n, me):
    if(me == "jug"):
        n,carta1,carta2= jugador(n)
    else:
        n,carta1,carta2= mesa(n)
       
    if(carta1 == 0):
        carta1 = 11
    
    if(carta2 == 0):
        carta2 = 11
    
    if (carta1+carta2 > 21):
        carta1=0

    s1=carta1+carta2
    print("suma",s1)
    return n


def run():
    """Juegos de cartas"""
    n=52

    print("------->NUMERACION DE CARTAS \n")
    print(cartas_corazon)
    n = primera_mano(n,"jug")
    n = primera_mano(n,"jug")
    n = primera_mano(n,"jug")
    n = primera_mano(n,"jug")

    n = primera_mano(n,"mesa")

    #print(baraja)
    #for i in range(1,27):  # prueba para ver todas las cartas
    #    print("jugador:",i)
    #    n,carta1,carta2=jugador(n)

    


if __name__ == '__main__':
    baraja = Merge(cartas_corazon, cartas_picas, cartas_diamante, cartas_trebol)
    juego_baraja = baraja.copy()

    run()