# Polimorfismo por subtipado
class Punto3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def modulo(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
    ## sebrecarga de metodo
    def to_tuple(self):
        return (self.x, self.y, self.z)

class Punto2D(Punto3D):
    def __init__ (self, x, y) :
        Punto3D.__init__(self, x, y, 0)
    def to_tuple(self):
        return (self.x, self.y)
    """
        #usando el metodo madre
        return Punto3D.to_tuple(self)[:2]
        #eliminado z    
        assert self.z == 0
        return Punto3D.to_tuple(self)
    """

class Punto1D(Punto2D):
    def __init__ (self, x) :
        Punto2D.__init__(self, x, 0)


punto = Punto2D(0, -2)
print(punto.modulo())

# herencia multiple
class Edificio(object):
    def __init__(self, nombre, recursos):
        self.nombre = nombre    
        self. recursos = recursos
    def producir(self):
        return '%s produce %s' %(self.nombre, self.recursos)

class Punto:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def modulo(self, other=None):
        if other is None:
            other = Punto(0, 0)
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

class EdificioUnico(Edificio, Punto):
    def __init__(self, nombre, recursos, x, y):
        Edificio.__init__(self, nombre, recursos)   
        Punto.__init__(self, x, y)

mina = EdificioUnico('Mina', ['Oro', 'Platino'], 0, 42)
print(mina.producir())
#"Mina produce ['Oro', 'Platino']"
print(mina.modulo())