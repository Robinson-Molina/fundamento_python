import sys

n1=input("Introduzca un primer numero:")

try:
    n1=int(n1)
except:
    print("La conversion de este numero no ha tenido exito",file=sys.stderr)
    sys.exit()
try:
    n2=int(input("Introduzca un segundo numero: "))
except ValueError as e:
    print("La conversion de este numero no ha tenido exito",file=sys.stderr)
    sys.exit()

suma=n1+n2
print("Las suma de los dos numero es:",n1,"+",n2,"=",suma)