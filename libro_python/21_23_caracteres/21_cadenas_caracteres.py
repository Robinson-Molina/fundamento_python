

import unicodedata

print(unicodedata.category("a"))

cadena="cadena"
numero=1
otra_cadena=""" Esto es una cadena en varias lineas 
Esto es una nueva linea  """

print(cadena, numero, otra_cadena)

def funcion():
    """
        Esta es la documentacion de la funcion
    """

print("¿Tu te insperas en %s?" % "C")
# el operador modulo solo recive dos operados: la cadena que se debe formatear a la izquierda y las variables que se inyectan a la derecha
print("¿Quieres la %s %s?" % ("pildora","azul"))

#con diCcionarios
print("¿Quien la %(obj)s %(color)s?" % {"obj":"pildora","color":"azul"})

#modulo ispirado en c++
print("¿Quieres la {} {} ?".format("pildora","azul"))

#permite modificar la posicion de la variables
print("Do you want the {1} {0}?".format("pill", "blue"))

#puede nombra los argumentos
print("¿Quieres la {obj} {color} ?".format(obj="pildora",color="azul"))

# poner en minusculas
cadena_minuscula = otra_cadena.lower()
print(cadena_minuscula)

# poner en mayusculas
cadena_mayusculas=otra_cadena.upper()
print(cadena_mayusculas)

cadena_mayusculas=otra_cadena.capitalize()
print(cadena_mayusculas)
# toda la palabra con la primera en mayuscula
cadena_mayusculas=otra_cadena.title()
print(cadena_mayusculas)
#la primera con minuscula y las demas con mayusculas
cadena_mayusculas=otra_cadena.swapcase()
print(cadena_mayusculas)

longitud=len(cadena)
print("la longitud es :",longitud)

pertenecia =cadena in otra_cadena
print("la cadena esta contenida en la otra: ", pertenecia)

# contar numero de ocurrencias
print("numero de A en cadena: ",otra_cadena.count("a"))

#encontrar posicion de ocurrencia
posicion=cadena.index("a")
print("indice: ",posicion+1)

posicion2=cadena.index("a", posicion+1)
print("indice: ",posicion2+1)

def posicion(cadena,fragmento):
    pos = -1
    for i in range(cadena.count(fragmento)):
        pos =cadena.index("a",pos + 1)
        print("Posicion n {}: caracter {}".format(i+1, pos))

posicion(otra_cadena,"a")

bus=cadena.find("a")
print("buscar caracter",bus + 1)

 # remplazo
cadena_nueva = cadena.replace("ca","[--OO--]")
print(cadena_nueva)

#listar Usar caracteres especiales
[chr(x) for x in range(191, 564)]


def run():
    #help(funcion)
    return

if __name__ == '__main__':
    run()