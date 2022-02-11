numero1=int(input("Introduzca un primer numero: "))
numero2=int(input("Introduzca un otro numero:"))

if(numero1 < numero2):
    print(numero1,"<",numero2)
elif(numero1> numero2):
    print(numero1,">",numero2)
else:
    print(numero1,"=",numero2)