lista = [0, 3, 7, 8, 2, 4, 1, 6, 5, 9]
lista.sort()
print(lista)

palabras ="Ah La frase a ordenar se ha daclrado con èxisto".split() # convireter alista las palabras

palabras.sort() ## ordena primero las mayusculas, minuscula y acentos 

print(palabras)

##uso de claves
palabras.sort(key=str.lower)
print(palabras)

#dicionario de caracteres acentos
"""
translation = str.maketrans(
    "àäâéèëêïîöôùüûÿŷç_-",
    "aaaeeeeiioouuuyyc ",
    "#~.?,;:!")

def transfromacion(x):
    return x.lower().translate(translation)

palabras.sort(key=transfromacion)
print(palabras)
"""