from array import array
from itertools import chain, product
from itertools import repeat,cycle

lista=list("abc")

for letra in lista:
    print(letra)

for indice, letra in enumerate(lista):
    print("indice {}, letra {} .".format(indice,letra))

##no hacer esto simmodificamos la una modificamos la otra
array=[lista,lista]
array[0][0]="X"
print("array= {}".format(array))
print("lista= {} \n".format(lista))


array1=[lista[:],[c.upper()for c in lista]]
array1[0][0]="X"
print("array1= {}".format(array1))
print("lista= {}".format(lista))

for linea in array1:
    for casilla in linea:
        print(casilla)

print("")
for casilla in chain.from_iterable(array1):
    print(casilla)

print("")

for i, linea in enumerate(array1):
    for j, casilla in enumerate(linea):
        print("array [{}][{}] = {}".format(i, j, casilla))

print("")

transpone=zip(*array)

for i, columna in enumerate(transpone):
    for j, casilla in enumerate(columna):
        print("array [{}][{}] = {}".format(i, j, casilla))

lineas = ["A", "B", "C"]
columnas = [1, 2, 3]

print("")
for linea, columna in product(lineas, columnas):
    print("Casilla {} {} ".format(linea, columna))

print("")
for linea, columa in zip(repeat("Z"), columnas):
    print("Casilla {} {} ".format(linea, columna))

print("")
for numero, letra in zip(range(10), cycle("ABC")):
    print("Casilla {} {}".format(letra, numero))