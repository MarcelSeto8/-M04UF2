#!/usr/bin/python3
import random

random = random.randint(0,100)

respuesta = ""

while respuesta != random:
	respuesta = int(input("Introduce un numero del 1 al 100: "))
	if random < respuesta:
		print("El numero que buscas es MENOR que " + str(respuesta))
	elif random > respuesta:
		print("El numero que buscas es MAYOR que " + str(respuesta))
	else:
		print("Lo adivinaste! El numero era " + str(random))
