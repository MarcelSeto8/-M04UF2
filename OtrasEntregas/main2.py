#!/usr/bin/python3
import random
import xmltodict
from player_class import Player
from enemies_class import Enemies

enemy = Enemies()
#primer_enemigo = enemy.enemies[1] #enemies es la array de Enemys
#print(primer_enemigo.name)
enemy.show_info()






#Abrimos el archivo, guardamos los datos en la variable data, cerramos el archivo donde tenemos los enemigos
#xml_file = open("enemies.xml")
#data = xml_file.read()
#xml_file.close()

#enemy_dict = xmltodict.parse(data)

#enemies = enemy_dict['enemies']['enemy']
current_enemy_index = 0

#Creamos el objeto player
player = Player("Juanjo")


turno = 1

while current_enemy_index < (len(enemy.enemies)):
	print("Experiencia Jugador: " + str(player.get_xp()))
	print("Level del jugador: " + str(player.get_level()))
	player.show_info()
	vidaPlayerInicioAtaque = player.get_health()
	gameEnemy = enemy.enemies[current_enemy_index]
	#print("\nNombre: " + str(enemy['name']))
	#print("Health: " + str(enemy['health']))
	#print("Strength: " + str(enemy['strength']))
	#print("Description: " + str(enemy['description']))
	gameEnemy.show_info()
	
	#enemy_health = enemy['health']

	while int(gameEnemy.health) > 0 and player.get_health() > 0:
	
		print()
		print("TURNO " + str(turno))
		print("La vida del heroe es: " + str(player.get_health()))
		print("La vida del enemigo es: " + str(gameEnemy.health))
		print()

		print("ES HORA DE QUE EL HEROE ATAQUE")
		print("==============================")
		action = input("¿Que acción quieres realizar?: ")
		if action == "ataca":
			gameEnemy.health = int(gameEnemy.health) - player.atack()
			print("La vida del enemigo despues del ataque es de: " + str(gameEnemy.health))
		else:
			print("Te quedaste mirando las musarañas")
	
		print()
		print("ES HORA DE QUE EL ENEMIGO ATAQUE")
		print("================================")
		enemy_atack = random.randint(0, 2)
		print("Atack of the enemy is: " + str(enemy_atack))
		player.set_health(player.get_health() - enemy_atack)
		turno += 1

	if player.isDeath():
		print("Mala suerte papu, PERDISTE")
		break
	if gameEnemy.health <= 0:
		print("Bien hecho! Acabaste con el enemigo " + gameEnemy.name +"!")
		player.add_xp(vidaPlayerInicioAtaque)		
		current_enemy_index += 1
