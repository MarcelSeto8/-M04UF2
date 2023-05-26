#!/usr/bin/python3

import xmltodict

fin = 0
salir = False
enemigos = []


def obten_datos():
	print("Vas a crear un enemigo: ")
	name = input("Name: ")
	health = int(input("Health: "))
	strength = int(input("Strength: "))
	description = input("Description: ")

	return {

		"name": name,
		"health": health,
		"strength": strength,
		"description": description

	}

def escribe_datos (export):
	
	enemy_xml = xmltodict.unparse(export, pretty=True)
	print(enemy_xml)
	xml_file = open("enemy.xml", "w")
	xml_file.write(enemy_xml)
	xml_file.close()

while not salir:
	opcion = input("¿Quieres añadir un enemigo?[s/N]")

	if opcion != "s":
		salir = True
		continue

	enemigo = obten_datos()
	enemigos.append(enemigo)

enemies_export = {
	"enemies": {
		"enemy": enemigos
	}
}

escribe_datos(enemies_export)
