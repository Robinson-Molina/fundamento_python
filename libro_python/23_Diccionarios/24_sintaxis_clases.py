
import math

class Miclase:
    """Documentacion"""
    def mi_metodo(self, nombre):
        print("{} .mi_metodo( {} ) ".format(self, nombre))



class Punto:
    """Representa un punto en el espacio"""
    
    def __init__(self, x, y, z,)-> None:
        """Metodo de inicializacion de un punto en el espacio"""
        self.x = x
        self.y = y
        self.z = z
    
    def mostrar (self):
        """Metodo temporal utilizado para mostrar muestro punto"""
        print("Punto( {}, {}, {})".format(self.x, self.y, self.z))
    
    def modulo(self):
        """Devuelve el modullo del punto"""
        modulo = math.sqrt(self.x**2 + self.y**2+ self.z**2)
        return modulo


    def distancia(self,Other):
        """
        Devuelve la distancia respecto a otro punto
        Las variables self y other son, ambas, puntos
        """
        distancia = math.sqrt((self.x - Other.x)**2 + (self.y - Other.y)**2 + (self.z - Other.z)**2)

        return distancia

    def distancia_y_modulo(self, Other=None):
        """Devuelve el modudo y la distancia respecto a otro punto por defecto al origen"""
        if Other == None:
            modulo1 = math.sqrt(self.x**2 + self.y**2+ self.z**2)
            distancia1 = math.sqrt((self.x - 0)**2 + (self.y - 0)**2 + (self.z - 0)**2)
        else:
            modulo1 = math.sqrt(self.x**2 + self.y**2+ self.z**2)
            distancia1 = math.sqrt((self.x - Other.x)**2 + (self.y - Other.y)**2 + (self.z - Other.z)**2)
        
        return modulo1, distancia1
    
    def __add__(self, otro):
        """ Devuelve la suma de ambos puntos. """
        return Punto(self.x + otro.x, self.y + otro.y, self.z + otro.z)
        
    def __sub__(self, Other):
        """Operador de resta"""
        return Punto(self.x - Other.x,
                     self.y - Other.y,
                     self.z - Other.z)
        
    def __mul__(self, Other):
        """Operador de multiplica"""
        return Punto(self.x * Other.x,
                        self.y * Other.y,
                        self.z * Other.z)
    def __iadd__(self, other):
        """Operador de adición en el lugar """
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    def __isub__(self, Other):
        """Operador de resta"""
        self.x -= Other.x
        self.y -= Other.y
        self.z -= Other.z
        return self
        
    def __imul__(self, Other):
        """Operador de multiplica"""
        self.x *= Other.x
        self.y *= Other.y
        self.z *= Other.z
        return self

    def __str__(self):
        """ Muestra el punto como de tres coordenada. """
        return "(" + str(self.x) + ", " + str(self.y) + ", "+ str(self.z)+")"
    
def run():
    mi_intancia = Miclase.mi_metodo("Mi clase","metodo")
    #Crear un punto
    p = Punto(1, 2, 3)
    q = Punto(1, 2, 5)
    # usar un metodo
    p.mostrar()
    
    print("|p|= ",p.modulo())
    print("La distancia entre p y (1, 2, 5) es ",p.distancia(Punto(1, 2, 5)))
    m,d= p.distancia_y_modulo()
    print("|p| =", m)
    m,d=p.distancia_y_modulo(Punto(1, 2, 5))
    print("la distancia entre p y (1, 2, 5) es ",d)
    print("la suma entre p y (1, 2, 5) es ",p + q)
    print("la resta entre p y (1, 2, 5) es ",p - q)
    print("la multiplicacion entre p y (1, 2, 5) es ",p * q)


if __name__ == '__main__':
    run()