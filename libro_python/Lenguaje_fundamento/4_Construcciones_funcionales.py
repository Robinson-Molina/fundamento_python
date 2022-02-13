## constructores funcionales
##variable = 42 if (film = "H2G2") else 0
##variable = 42 if (film = "H2G2") else 1 if (film= = "aventure") else 0
##(funcion1 if (film = "H2G2") else funcion2)()
##instance = (Class1 if (film = "H2G2") else Class2)()

# Generador infinito

gen = (a**2 for a in range(1000))
#gen=(a**2 for a in generador_infinito())
gen= (a**2 for a in range(1000) for b in range(1000))

# Lista recorido

lista = [a**2 for a in range(1000)]
lista = [a+b for a in range(1000) for b in range(1000)]

# recorido de conjunto

conjunto = {a**2 for a in range(1000)}

# recorido de dicionario

diccionario = {a: a**2 for a in range(1000)}
tabla = {(a, b): a*b for a in range(1000) for b in range(1000)}