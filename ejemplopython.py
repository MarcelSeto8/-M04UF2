def suma_numeros (a, b):
   print(a + b)

num1 = 8
num2 = 12

print("ola k ase")	

if num1 > num2:
	print(str(num1) + " es mayor que " + str(num2))
elif num1 < num2:
	print(str(num2) + " es mayor que " + str(num1))
else:
	print("Son iguales")

contador = 10

while contador > 0:
	print(contador)
	contador -= 1

teclado = input("Introduce tu nombre: ")
print("Hola " + teclado)




lista = ["uno", 2, "tres"]

print(len(lista)) #len se utiliza para saber los caracteres de una string o el tamaño de una array

suma_numeros(7, 9)
