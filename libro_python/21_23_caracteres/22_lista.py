
lista=list("Python is awesome")

print(lista)

#indices
print(lista[4])

#ppara partir del final
print(lista[-3])

#un rango
print(lista[2:6])

#utilizar paso puede ser negativo
print(lista[2::5])

print(lista)

#asignacion
lista[11]="b"
print(lista)

lista[13:15]="fg"
print(lista)

# eliminiar elemento
del lista[15]
print(lista)

#del lista[:7]
#print(lista)

#eliminar sin saber su indice
lista.remove("i")   
print(lista)

while " " in lista:
    lista.remove(" ")
print(lista)

# elimininar ultimo valor
lista.pop()
print(lista)

#agregar valor al 
lista.append("h")
print(lista)

lista.insert(2,"d")
print(lista)

lista.extend(["i","j"])
print(lista)


def ejercio1():
    lista1=["P","t"]
    # todo
    lista1.extend(["hon"])
    lista1.insert(1,"y")
    
    try:
        assert "".join(lista1)== "Python"
    except AssertionError as e:
        print("No funiciona no conside la lista 1")

def ejercio2():
    lista2=[1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9]
    
    # todo
    print(list(range(1,6,2)))
    while 4 in lista2:
        lista2.remove(4)

    lista2.pop()
    lista2.pop()
    del lista2[2]
    lista2.remove(2)
    lista2.remove(7)

    print(lista2)
    try:
        assert lista2== list(range(1,6,2))
    except AssertionError as e:
        print("No funiciona no conside la lista 2")        

ejercio1()
ejercio2()