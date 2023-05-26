#!/usr/bin/python3
import random
import xmltodict

list_of_enemyfiles = ["enemy1.xml", "enemy2.xml", "enemy3.xml"]
file_enemy = random.choice(list_of_enemyfiles)

xml_file = open(file_enemy)
data = xml_file.read()
xml_file.close()

enemy_dict = xmltodict.parse(data)
enemy = enemy_dict['enemies']['enemy']

hero_health = 100
enemy_health = enemy['health']
turno = 1

print("\nNombre: " + str(enemy['name']))
print("Health: " + str(enemy['health']))
print("Strength: " + str(enemy['strength']))
print("Description: " + str(enemy['description']))


while int(enemy_health) > 0 and hero_health > 0:
	print()
	print("TURNO " + str(turno))
	print("La vida del heroe es: " + str(hero_health))
	print("La vida del enemigo es: " + str(enemy_health))
	print()

	print("ES HORA DE QUE EL HEROE ATAQUE")
	print("==============================")
	action = input("¿Que acción quieres realizar?: ")
	if action == "ataca":
		hero_atack = random.randint(0, 5)
		print("Atack of the hero is: "+ str(hero_atack))
		enemy_health = int(enemy_health) - hero_atack
	else:
		print("Te quedaste mirando las musarañas")
	
	print()
	print("ES HORA DE QUE EL ENEMIGO ATAQUE")
	print("================================")
	enemy_atack = random.randint(0, 2)
	print("Atack of the enemy is: " + str(enemy_atack))
	hero_health -= enemy_atack
	turno += 1

if hero_health <= 0:
	print("Mala suerte papu, PERDISTE")
if int(enemy_health) <= 0:
	print("Bien hecho! Acabaste con él!")
