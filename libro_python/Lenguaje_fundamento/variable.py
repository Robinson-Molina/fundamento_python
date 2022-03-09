import asyncio 
import random

ejemplo = 3+5
ejemplo2 = ejemplo + 1.0

print (type(ejemplo))
print(type(ejemplo2))

#Esta palabra clave is también puede utilizarse para realizar comparaciones no sobre valores, 
# sino sobre objetos

ejemplo3 =ejemplo

print(ejemplo2 is ejemplo)
print(ejemplo3 is ejemplo)

print(42 == 42.0)
print(42 is 42.0)

#condición is True
#variable is None

a, b, c, d, e, f = 1, *(2, 3), 4, *range(5, 6), 6

print(a);print(b);print(c)
print(d);print(e);print(f)

#funciones anonimas
f = lambda x: x**2
print(f(5))
L = list(map(f, range(10)))
print(L)

g = lambda x, y: x*y**2
print(g(4, 2))

# eliminar variables y funciones
a=5
del a

b=list(range(10))
print(b)
del b[5] #índice
del b[2:7:2] #franja
print(b)

# multiples asignaciones
def f():
    return 1, 2, 3

a,b,c = f()
print(a,b,c)


condicion = a in (2, 3, 5, 7, 11, 13)
#a == 2 or a == 3 or a == 5 or a == 7 or a == 11 or a == 13
print(condicion)

# for con in intera en cada elemento de la tupla
for a in (5, 7, 11, 13):
    print('%d es un número primo' % a)



#iterar asicronamente

cursor=2,3,4,5,6
#async for row in cursor:
#    print(row)

