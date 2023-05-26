#!/usr/bin/python3
import random

def suma_numeros(a, b):
	print(a + b)

num1 = 333
num2 = 666

if num1 > num2:
	print("El numero " + str(num1) + " es mayor que el numero " + str(num2))
elif num1 < num2:
	print("El numero " + str(num2) + " es mayor que el numero " + str(num1))
else:	
	print("Los números son iguales")

suma_numeros(num1, num2)
