from http.client import ImproperConnectionState


from random import choice, sample, shuffle

cartas=[chr(x) for x in range(0x1f0a1, 0x1f0af)]

print(cartas)
escoger_carta = choice(cartas)

cartas_selec = sample(cartas,5)

Aleatorio_cartas = shuffle(cartas) # mescla y no retoruna none

print(cartas)
print(escoger_carta)
print(cartas_selec)
print(Aleatorio_cartas)