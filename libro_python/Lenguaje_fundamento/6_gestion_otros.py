# modulos
from calendar import c
from math import sqrt as raiz
print(raiz(9))


#<built-in function sqrt>
#import cmath as math_complejos

import pdb
print(dir(pdb))


class A:
    """Descripción de mi clase"""
    atributo = "Esto es un atributo"
    def método(self, *args, **kwargs):
        return "Esto es un método"

A.__doc__
#’Descripción de mi clase’
A.atributo
#’Esto es un atributo’
A.método
#<function método at 0x257ea68>

class Declarativa(object):
    """Clase escrita de manera declarativa"""
    atributo_de_clase = 42

    def __init__(self, name):
        self.name = name
        self.subs = []

    def __str__(self):
        return "{} ({})".format(self.name, ", ".join(self.subs))
    def mostrar(self):         
        print(self)

#agregar atributos a la clase
a = Declarativa("test")
a.subs.append("cosa")
a.subs.append("chisme")
print(a, "\n")
#test (cosa, chisme)
print(dir(a))

# agregar un metodo a una clase
def mostrar(self):
    print(self)
a.mostrar = mostrar

a.mostrar(2)

# Tuplas con nombre
from collections import namedtuple

Punto = namedtuple('Punto', ['x', 'y'])
p = Punto(4, 2)
print(p)

#los métodos de instancia, donde por convención el primer argumento se llama
#self y representa a la instancia:
# 
# los métodos de clase, donde por convención su primer argumento se llama
#cls y cuya característica importante es que representan a la clase: 
# 
# los métodos estáticos, que tienen una firma idéntica a las funciones. Se trata de funciones agregadas a las clases:
class A:
    def metodo_instancia(self, *args, **kwargs):
        return "Esto es un método de instancia"

@classmethod
def metodo_clase(cls, *args, **kwargs):
    return "Esto es un método de clase aplicado sobre %s" % cls

@staticmethod
def metodo_estatico(*args, **kwargs):
    return "Esto es un método estático"


## representacion

for a in [1, "1", int, list([1]), tuple({1}), set((1,)),dict([(1, 1)])]:
    repr(a), str(a)

#(’1’, ’1’)
#("’1’", ’1’)
#("<class ’int’>", "<class ’int’>")
#(’[1]’, ’[1]’)
#(’(1,)’, ’(1,)’)
#(’{1}’, ’{1}’)
#(’{1: 1}’, ’{1: 1}’)

class a(object):
    def atributo(self):         
        print(self)

# manera de comprobar si exite un metodo y agregarlo de clase a
if hasattr(a, 'atributo'):
    getattr(a, 'atributo')
    print("True")
else:
    setattr(a, 'atributo', 'valor')
    print("False")

# Relación entre objetos

class Punto:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def module(self, other=None):
        if other is None:
            other = Punto(0, 0)
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

p1 = Punto(2, -3)
p2 = Punto(2, 4)
print(p1.module(p2))
