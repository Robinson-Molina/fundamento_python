from calendar import c
import imp


agenda={
    "Climent" : "601020304",
    "Claudia" : "934123456",
    "Mateo" : "917101345",
}

print(agenda["Claudia"])

agenda["Sebatian"]="791827364"

print(agenda)


for nombre, telefono in agenda.items():
    print("El numero de  {} es {}".format(nombre,telefono))

#listar ordenadamente
print("")
for nombre in sorted(agenda.keys()):
    print("El numero de  {} es {}".format(nombre, agenda["Mateo"]))

#comprobar si exite
print("Casiopea" in agenda)

print(agenda.get("Casiopea"))

print (agenda.get("Casiopea","987654321"))

print(agenda)
print("\n")
##juego de cartas
from random import choice, sample

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

lista_cartas=list(cartas)

carta1= choice(lista_cartas)

score= cartas[carta1]

carta2= choice(lista_cartas)

score= cartas[carta1]+cartas[carta2]

print("Ha selecionado {} {} y tu puntuacion es: {}".format(carta1,carta2,score))

main_banca=sample(lista_cartas, 2)
score_banca =sum(cartas[carta] for carta in main_banca)

print("La banca tiene {} y puntuacion es: {}".format(main_banca,score_banca))


