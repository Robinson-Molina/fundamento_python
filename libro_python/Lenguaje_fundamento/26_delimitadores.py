import asyncio
## uso de ; par ejecucion en una sola linea
#import pdb; pdb.set_trace()

# Muestra las palabras reservadas en consola
#import keyword
#keyword.kwlist

# @indetiacion en una sola linea 
from curses import curs_set
from sqlite3 import Cursor
from time import process_time_ns


a=0
for i in range(10): a += 1; print(a)

# para no usar indentacion se puede regresar a las llaves
#from __future__ import braces

## generador
g = (i**2 for i in range(10))

#listas
l=[i**2 for i in range(10)]
print(l)

#conjuntos o diccionarios con llaves 
diccionario = {'claves1':'valor1','clave2':'valor2','clav3':'valor3'}
conjunto = {1, 2, 3}

## diccionario con recorrido
d = {chr(i): chr(i+32) for i in range(65, 91)} # mayusculas con miniculas
e={i**2 for i in range(10)}
## delimitar franjas
print(l[1:])

##No existen los símbolos $ , ? o ` 
##De este modo, si bien este carácter es meramente convencional, el resultado puede ser poco satisfactorio. Python proporciona otro mecanismo,
#algo más complejo, para hacer inaccesibles los atributos o métodos privados. Para utilizar este mecanismo, basta con prefijarlos con dos
#caracteres de subrayado (u opcionalmente puede agregarse como sufijo un único carácter de subrayado).

#  punteros
ejemplo=4*10+2
ejemplo2=ejemplo*1.0
ejemplo3=ejemplo

ejemplo is ejemplo2  # False
ejemplo3 is ejemplo  #True

#Esta palabra clave is también puede utilizarse para realizar comparaciones no sobre valores, sino sobre objetos

a, b, c, d, e, f = 1, *(2, 3), 4, range(5, 6), 6

# El carácter * sirve para transformar un contenedor de valores para utilizarlos en el flujo. La función
# todos los valores entre un mínimo incluido y un máximo excluido.

## Funciones anonimas

f = lambda x: x**2
f(5)
#25
Li=list( map(f, range(10)))
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = lambda x, y: x*y**2
g(4, 2)
#16

## Borrado

b=list(range(10))
del b[5] #índice
del b[2:7:2] #franja

#[0, 1, 3, 6, 8, 9]
c={'a': 'A', 'b': 'B','c': 'C'}
del c['b'] # clave

#{’a’: ’A’, ’c’: ’C’ }

### concadenar las operaciones siempres se evalia de izquierda a derecha
# in par verificar si el valor o los valores se encuentran
a in (2, 3, 5, 7, 11, 13)

#La palabra clave in verifica la pertenencia de un elemento a una secuencia. La combinación de esta con la palabra clave for permite iterar
#sobre el conjunto de elementos de la secuencia.
for a in (5, 7, 11, 13):
    print('%d es un número primo' % a)

#5 es un número primo
#7 es un número primo
#11 es un número primo
#13 es un número primo

# Uso de manera asincrono
"""
import asyncio

async def ping_server(ip):
    pass

@asyncio.coroutine
def load_file(path):
    pass
"""

def test():
    brk, num = False, 0
    for a in range(1, 20, 2):
        for b in range(1, 20, 3):
            if a == b:
                print(a)
                num += 1
                if num >= 2: brk=True
                break
        if brk:
            break

test()

def f():
    a = 1
    while True:
        a *= 2
        if a > 1000000:
            return a

print(f())

#Otra instrucción extremadamente útil es continue . Permite, simplemente, interrumpir una iteración para pasar a la siguiente. He aquí un ejemplo:
print("comtinue")
def positivo(l):
    for a in l:
        if a < 0:
            continue
        print(a)

print(positivo((6,7)))

## imprimir los valores primos 
for n in range(2,10):
    x=2
    while x < n:
        if n % x == 0:
            print('%i vale %i * %i' % (n,x,n/x))
            break
        print(x)
        x += 1
    else:
        print('%i es un numero primo' %n)

## Generadores

def g(num):
    for i in range(num):
        print('Generador %d' % i)
        yield i 

gen = g(4)
print(gen)

for i in gen:
    print('Uso %d' % i)

## uso de yield from

def cadena(*iters):
    for it in iters:
        for item in it:
            yield item

def cadena1(*iters):
    """Permite separa cadenas"""
    for it in iters:
        yield from it


Cd=cadena("cadena")
Cd1=cadena1("cadena")

for i in Cd:
    print('separa %s' % i)

for i in Cd1:
    print('separa con yield from %s' % i)
