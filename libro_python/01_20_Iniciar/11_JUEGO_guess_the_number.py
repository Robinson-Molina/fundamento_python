import random
import sys

numero=random.randint(0,100)
n=10
while n>0:
    print("Encuentre el numero que pienso")
    while True:
        
        intento=input("Escriba el numero: ")

        try:
            intento=int(intento)
        except ValueError as e:
            pass
        else:
            if 0<= intento <=100:
                break
    
    if intento > numero:
        print("-----Demasiado Grande-----")
        n=n-1
        print("te quedan:", n)
    elif intento < numero:
        print("-----Demasiado Pequeño-----")
        n=n-1
        print("te quedan:", n)
    else:
        print("\n!!!Ha ganado!!!")
        n=0

