#!/usr/bin/python3
import random
import xmltodict
import json
class Player: 
	
	def __init__ (self,name="", health = "", strength = "", level = "", xp = "", description = ""):
		#Creamos el constructor de Player con los valores pasados por parámetro
		self.name = name
		self.description = description
		self.health = health
		self.strength = strength	
		self.level = level
		self.xp = xp
		
		#Parseamos los levels y la xp que requiere cada nivel para poderlos usar con las instáncias de player
		xml_file = open("levels.xml", "r")
		levels = xmltodict.parse(xml_file.read())
		xml_file.close()

		tmp = levels["levels"]["level"]
		self.levels = {}

		for level in tmp:
			self.levels[ int(level["@num"]) ] = int (level["@xp"])
		

	def set_health (self, health):
		self.health = health
	
	def get_health (self):
		return self.health
	
	def hurt(self, _atackEnemyTurn):
		self.set_health(self.get_health() - _atackEnemyTurn)

	def set_strength (self, strength):
		self.strength = strength
	
	def get_strength (self):  
		return self.strength

	def atack(self):
		return random.randint(0, self.strength)

	def set_xp (self, xp):
		self.xp = xp

	def get_xp (self):
		return self.xp
	
	def add_xp (self, _vidaPlayerInicioAtaque):	#Experiéncia a recibir: nº al azar (entre 1 y el lvl del player) * vida del player al inicio del ataque
		experienciaRecibir = self.get_xp() + (random.randint(1, self.level) * _vidaPlayerInicioAtaque)
		self.set_xp(experienciaRecibir)

	def set_level (self, level):
		self.level = level

	def get_level (self):
		current_xp = self.xp
		current_level = self.level

		for level in self.levels:
			required_xp = self.levels[level] #xp del xml
			if current_xp >= required_xp:
				current_level = level #num level del xml
		return current_level
	
	def level_up (self, _levelBeforeCombat, _levelAfterCombat):
		if _levelBeforeCombat != _levelAfterCombat:
			self.set_level(self.get_level())
			if (_levelAfterCombat - _levelBeforeCombat) == 1:
				print("Congratulations you have gone up 1 level!") 
			else:
				print("Congratulations you have gone up " + str(_levelAfterCombat - _levelBeforeCombat) + " levels!")

	def isDeath (self):
		return (self.get_health() <= 0)
	
	def show_info (self):
		print("____________DATOS HERO___________")
		print("Name: " + self.name)
		print("Health: " + str(self.health))
		print("Strength: Between 0 - " + str(self.strength))
		print("XP: " + str(self.xp))
		print("Level: " + str(self.level))
		print("Description: " + self.description)
	
	def input_info (self): #Para los parámetros no predeterminados del player
		self.name = input("Introduce el nombre: ")
		self.description = input("Introduce una descripción para tu personaje: ")
		print("Los otros valores han sido asignados de manera predeterminada para que el juego se ejecute de manera balanzeada")

	def write_info_xml (self): #Para escribir datos de guardado de partida en formato xml
		info = {
			"name":self.name,
			"health":self.health,
			"strength":self.strength,
			"level":self.level,
			"xp":self.xp,
			"description":self.description
		}

		player_info = {
			"player":info
		}

		xml_file = open("player.xml", "w")
		xml_file.write(xmltodict.unparse(player_info, pretty=True))
		xml_file.close()
	
	def write_info_json (self): #Para escribir datos de guardado de partida en formato json
		
		info = {
			"name":self.name,
			"health":self.health,
			"strength":self.strength,
			"level": self.level,
			"xp": self.xp,
			"description":self.description
		}

		player_info = {
			"player":info
		}

		with open("player.json", "w") as json_file: #con el with se cierra el archivo de forma automática
			json.dump(player_info, json_file, indent=4)

	def read_info_xml (self): #Recuperar datos guardados del formato xml
		xml_file = open("player.xml", "r")
		player_tmp = xmltodict.parse(xml_file.read())
		xml_file.close()

		player = player_tmp["player"]
		
		name = player["name"]
		health = int(player["health"])
		strength = int(player["strength"])
		level = int(player["level"])
		xp = int(player["xp"])
		description = player["description"]

		return Player(name, health, strength, level, xp, description)

	def read_info_json (self):
		with open("player.json", "r") as json_file:
			player_tmp = json.load(json_file)

		player = player_tmp["player"]
		name = player["name"]
		health = int(player["health"])
		strength = int(player["strength"])
		level = int(player["level"])
		xp = int(player["xp"])
		description = player["description"]

		return Player(name, health, strength, level, xp, description)
