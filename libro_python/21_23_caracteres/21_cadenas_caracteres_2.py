import string

print(string.ascii_letters)

print(string.ascii_lowercase)

print(string.ascii_uppercase)

print(string.digits)

print(string.hexdigits)

print(string.octdigits)

print(string.punctuation)

print(string.whitespace)

print(string.printable)

letra="1"

if letra in string.digits :
    print("la letra {} es una cifra. ".format(letra))

frase="esta es la palabra que se vera"

palabra=frase.split()
print(palabra)

pegamento="<pegamento>".join(palabra)
print(pegamento)

lista_caracteres=list(frase)
print(lista_caracteres)
