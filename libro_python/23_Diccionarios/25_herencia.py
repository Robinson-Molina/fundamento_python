
import math 

# las clases MostrableMixin y NombreAutomatic no funcionan???? hoja 86 del libro
class MostrableMixin:

    str_format = "PrettyPrintableObject"

    def __str__(self):
        """
        Represntacion automatica de un objeto,
        basado en el uso de una cadena de formateo 
        que es un atributo de la clase
        """
        return self.str_format.format(self=self)

class NombreAutomaticMixin:

    ordinal = 65

    def __int__(self):
        self.letra= chr(NombreAutomaticMixin.ordinal)
        NombreAutomaticMixin.ordinal += 1


class Punto ():
    """Representa un punto en el espacio"""
    str_format="Punto {self.letra} ({self.x}, {self.y}, {self.z})"
    
    def __init__(self, x, y, z,)-> None:
        """Metodo de inicializacion de un punto en el espacio"""
        super().__init__()
        self.x, self.y, self.z = x, y, z
    
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
        distancia = math.sqrt((self.x - Other.x)**2 \
                            + (self.y - Other.y)**2 \
                            + (self.z - Other.z)**2)

        return distancia

    def distancia_y_modulo(self, Other=None):
        """Devuelve el modudo y la distancia respecto a otro punto por defecto al origen"""
        if Other == None:
            modulo1 = math.sqrt(self.x**2 + self.y**2+ self.z**2)
            distancia1 = math.sqrt((self.x - 0)**2 + (self.y - 0)**2 + (self.z - 0)**2)
        else:
            modulo1 = math.sqrt(self.x**2 + self.y**2+ self.z**2)
            # el uso de \ como salto de linea no debe ser seguido de # comentario
            distancia1 = math.sqrt((self.x - Other.x)**2 \
                                    + (self.y - Other.y)**2 \
                                    + (self.z - Other.z)**2) 
        
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
    
class Punto2D (Punto):
    """Representa un punto en el plano"""
    str_format="Punto 2D {self.letra} ({self.x}, {self.y})" 
    def __init__(self, x, y) -> None:
        super().__init__(x, y, 0)
    
    def __str__(self):
        return "Punto2D es: ({self.x}, {self.y})".format(self=self)


def run():
    
    q=Punto(1, 2, 3)
    print(q)
    p=Punto2D(1, 2)
    p+=Punto2D(3, 0)

    print(p)

if __name__ == '__main__':
    run()