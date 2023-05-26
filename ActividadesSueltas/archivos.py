#!/usr/bin/python3

try: 
	archivo = open("numeritos.txt", "r")
	linea = archivo.readline()
	lista = linea.split(";")
	print(lista[2])
	archivo.close()
except:
	print("Error al abrir el archivo")

archivo = open("textitos.txt", "w")
archivo.write("ola k ase papu")
archivo.close()

diccionario = {
	"nombre": "Marcel",
	"apellido": "Setó",
	"edad": 21
}

print(diccionario["edad"])
	
