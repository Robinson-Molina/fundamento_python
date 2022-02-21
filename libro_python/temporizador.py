## Contador de terminal
from datetime import datetime
import time
#from pygame import mixer

def comprobar(test,l):
    """Comprobar que se cumpla el formato y sacar los tiempos"""
    contador = len(l)
    logi=contador
    v=0
    horas = 0
    minutos = 0
    segundos = 0
    
    while contador-1 >= 0:
        #print("Este el valor a evaluar",l[contador-1])
        if ":" == l[contador-1]:
            numero = ""
            v += 1
            for i in range (contador,logi):
                if ":" == l[i]:
                    break
                #print(l[i])
                numero =numero + l[i]
                

            if v == 1:
                segundos = int(numero)
                print("los segundos:",segundos)
            elif v == 2:
                minutos = int(numero)
                print("los minutos:",minutos)
            elif v == 3:
                horas = int(numero)
                print("los hora:",horas)
            
        contador-=1     


    if v == 3:
        pass
    else:
        print("No cumple el formato:"+ str(test))
    
    return horas,minutos,segundos

def contador(h,m,s):
    """Calcular las cantidades de tiempo a emplear """
    print("\n Es hora de iniciar conteo")

    tiempo=h*60*60+m*60+s
    print("Tiempo en ciclo :", tiempo)
    while tiempo > 0:
        fecha= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(fecha)
        tiempo -= 1
        time.sleep(1)



def run():
    print("\n Ingresa un el tiempo 00:00:00")
    datos = input()
    lista = list(datos)
    #print(lista)
    hor,min,seg = comprobar(datos,lista)
    contador(hor, min, seg)


if __name__ == "__main__":
	run()
