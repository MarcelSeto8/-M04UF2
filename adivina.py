import random

random = random.randint(0, 100)
print(random)
numeroPreguntado = -1

while numeroPreguntado != random:
	numeroPreguntado = input("Digite el numero: ")
	numeroPreguntado = int(numeroPreguntado)
	if numeroPreguntado > random:
		print(str(numeroPreguntado) + " es mayor que el numero que buscas")
	elif numeroPreguntado < random:
		print(str(numeroPreguntado) + " es menor que el numero que buscas")
	else:
		print("Felicidades!!! " + str(numeroPreguntado) + " es igual a " + str(random)) 

