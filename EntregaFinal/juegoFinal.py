#!/usr/bin/python3
import time
import os
from game_class import Game
from player_class import Player
from enemies_class import Enemies


while True:
	os.system("clear")
	print("Bienvenido al juego de la python")
	print("1. Nueva Partida")
	print("2. Cargar Partida")
	print("3. Salir")
	optionInitGame = input("Que acción desea realizar: ")
	os.system("clear")

	if optionInitGame == "1":
	
		#Creando Player
		print("Cargando la creación del jugador...")
		time.sleep(3)
		os.system("clear")
		name = input("Escribe el nombre de tu personaje: ")
		description = input("Escribe la descripción de tu personaje: ")
		player = Player(name, 100, 5, 1, 0, description)
		os.system("clear")
		print("Procesando datos...")
		time.sleep(3)
		os.system("clear")
	
		#Carga enemigos en xml o json
		print("¿Como desea generar los enemigos?")
		print("1. Cargar enemigos con XML")
		print("2. Cargar enemigos con JSON")
		xmlOrJson = input("Digite la opción que desee: ")
		enemy = Enemies(xmlOrJson, int(optionInitGame))
		os.system("clear")

		#Creando partida
		print("Creando partida...")
		time.sleep(3)
		os.system("clear")
		game = Game(player, enemy)
		game.gamePython()

	elif optionInitGame == "2":

		# Recuperamos el último player guardado
		os.system("clear")
		print("Cargando datos des de la última vez que se guardo...")
		time.sleep(3)
		os.system("clear")
		print("¿Como desea recuperar los datos del player guardado?")
		print("1. Cargar player en XML")
		print("2. Cargar player en JSON")
		xmlOrJson = input("Digite la opción que desee: ")
		
		player = Player()
		if xmlOrJson == "1":
			player = player.read_info_xml()
		elif xmlOrJson == "2":
			player = player.read_info_json()
		os.system("clear")
		print("Procesando datos...")
		time.sleep(3)
		os.system("clear")
		
		# Recuperamos a los enemigos guardados en xml o json
		print("¿Como desea recuperar los datos de los enemigos guardados?")
		print("1. Cargar enemigos en XML")
		print("2. Cargar enemigos en JSON")
		xmlOrJson = input("Digite la opción que desee: ")
		os.system("clear")
		enemy = Enemies(xmlOrJson, int(optionInitGame)) #puede que el primero esta mal

		#Creando partida
		print("Cargando partida...")
		time.sleep(3)
		os.system("clear")
		game = Game(player, enemy)
		game.gamePython()

	elif optionInitGame == "3":
		print("Saliendo de la partida...")
		time.sleep(3)
		os.system("clear")
		break

	else:
		print("El numero seleccionado no corresponde a ninguna opcion")
		time.sleep(3)
		os.system("clear")

