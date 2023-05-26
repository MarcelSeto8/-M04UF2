#!/usr/bin/python3
import random
import time
import os
import xmltodict
from player_class import Player
from enemies_class import Enemies

class Game:
	
	def __init__ (self, player, enemy): 
		
		#Creamos el constructor de la classe Game pasandole el player y los enemigos que queremos que juegen la partida
		self.enemy = enemy
		self.player = player

	def gamePython (self):
		
		playerInitialStrength = self.player.get_strength() #Nos guardamos la strength inicial para calcular la xp del player a posterior
		turno = 1
		action = ""

		while (len(self.enemy.enemies)) > 0: #Mientras que la array de enemies sea mayor a 0, el juego seguirá en marcha
			print("===============================")
			self.player.show_info() #Nos muestra la información del player
			print("===============================")
			vidaPlayerInicioAtaque = self.player.get_health()
			levelPlayerBeforeCombat = self.player.get_level()
	
			gameEnemy = self.enemy.enemies[0]
			gameEnemy.show_info()
			print("===============================")
			time.sleep(10)
			os.system("clear")

			while gameEnemy.get_health() > 0 and self.player.get_health() > 0: 
				print("==============================")	
				print("TURNO " + str(turno))
				print("La vida del heroe es: " + str(self.player.get_health()))
				print("La vida del enemigo es: " + str(gameEnemy.get_health()))
				print("==============================")

				print("ES HORA DE QUE EL HEROE ATAQUE") #Acción a realizar del player
				print("==============================")
				action = input("¿Que acción quieres realizar? (ataca / guardar): ")
				print("==============================")

				if action == "ataca":
					atackPlayerTurn = self.player.atack()
					gameEnemy.hurt(atackPlayerTurn)
					print("Atack of the hero is: " + str(atackPlayerTurn))

				elif action == "guardar": #Guardamos toda la información tanto en XML como en JSON
					self.enemy.write_info_xml()
					self.player.write_info_xml()
					self.player.write_info_json()
					self.enemy.write_info_json()
					break

				else: #Si la opción que elijes no es una de las posibles
					print("Te quedaste mirando las musarañas")
	
				print("================================") #Turno de ataque del enemigo
				print("ES HORA DE QUE EL ENEMIGO ATAQUE")
				print("================================")
				atackEnemyTurn = gameEnemy.atack()
				self.player.hurt(atackEnemyTurn) 
				print("Atack of the enemy is: " + str(atackEnemyTurn))
	
				turno += 1
				print("================================")
				time.sleep(4)
				os.system("clear")

			if action == "guardar": #Si decides guardar
				os.system("clear")
				print("Guardaste correctamente la partida...")
				time.sleep(3)
				break
			if self.player.isDeath(): #El player está muerto?
				os.system("clear")
				print("GAME OVER: Mala suerte papu, PERDISTE")
				time.sleep(3)
				break
			if gameEnemy.isDeath(): #El enemigo está muerto?
				print("===========================================================")
				print("Bien hecho! Acabaste con el enemigo " + gameEnemy.name +"!")
				self.enemy.enemies.pop(0) # Elimina el primer elemento de la array de enemigos (el que ya está muerto)
				self.player.add_xp(vidaPlayerInicioAtaque) #Actualizamos xp del enemigo
				self.player.level_up(levelPlayerBeforeCombat, self.player.get_level()) #Comprobamos si el nivel del player se tiene que actualizat	
				self.player.set_strength((playerInitialStrength * self.player.get_level())) #Actualizamos la fuerza del player
				print("============================================================")
				time.sleep(5)
				os.system("clear")
				if len(self.enemy.enemies) <= 0: #Si ya no quedan enemigos, ganaste el juego.
					os.system("clear")
					print("YOU WIN: Enhorabuena ganaste la partida")
					time.sleep(5)
