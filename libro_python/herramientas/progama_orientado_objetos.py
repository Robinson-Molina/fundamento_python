import csv
class File:
    def __iter__(self):
        return self
    def __next__(self):
        raise StopIteration

file = File()
csv.reader(file)

# Condicionar el acceso de atributos
class A:
    read_only = ['x', 'y']
    x, y, z = 'X','Y', 'Z'
    def __setattr__(self, name, value):
        if name in self.read_only:
            raise Exception('Read only attribute')
        else:
            return object.__setattr__(self, name, value)
    def __delattr__(self, name):    
        if name in self.read_only:
            raise Exception('Read only attribute')
        else:
            return object.__delattr__(self, name)

a = A()
print(a.x)
## no se puede modificar x  Y
#a.x=1

print(a.z)
a.z=1
print(a.z)
#read_olny puedes ser modificado
# a.read_only.pop(0)


#Propiedades
#Las propiedades son un mecanismo particular, técnico, 
# destinado a permitir el uso de un método como un atributo

class Boletín:
    def __init__(self, *notas):
        self.notas = list(notas)
    @property
    def media(self):
        if len(self.notas):
            #print(len(self.notas))
            return sum(self.notas)/len(self.notas)
        return 0
    @property
    def ultima_nota(self):
        if len(self.notas):
            return self.notas[-1]
        return None
    @ultima_nota.setter
    def ultima_nota(self, nota):
        self.notas.append(nota)
    @ultima_nota.deleter
    def ultima_nota(self):
        self.notas.pop()

b=Boletín(12,12,5)
print(b.media,b.ultima_nota)
b.ultima_nota = 10
print(b.media)

#Es posible condicionar la escritura de las propiedades en función de una necesidad funcional concreta y, de este modo, controlar su visibilidad,
#incluso prohibiendo su modificación y su borrado:
class A(object):
    __attr = 0
    @property
    def atributo(self):
        return self.__attr

a = A()
#a.atributo = 42  # no se puede accede  

#Ubicacion

class A:
    __slots__ = ['a']

a=A()

a.a=1
a.b=1