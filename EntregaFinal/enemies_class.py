#!/usr/bin/python3

import xmltodict	
import json
from enemy_class import Enemy

class Enemies:

	def __init__(self, _xmlOrJson, iniciar_o_cargar): #La variable iniciar_o_cargar es para saber si tenemos que iniciar la partida de zero o cargarla, la variable _xmlOrJson es para saber si queremos abrir en formato xml o json.
		self.enemy_counter = 0
		
		if int(_xmlOrJson) == 1:
			self.loadWithXml(iniciar_o_cargar)
		
		if int(_xmlOrJson) == 2:
			self.loadWithJson(iniciar_o_cargar)

		
	def show_info(self): #Nos da la información del enemy que hay en ese turno
		self.enemies[self.enemy_counter].show_info()

	def loadWithXml(self, iniciar_o_cargar): #Tratar datos con XML
		self.enemies = []

		if iniciar_o_cargar == 1: #Iniciar partida desde zero
			xml_file = open("enemies.xml", "r")
			enemies_tmp = xmltodict.parse(xml_file.read())
			xml_file.close()

			enemies_list = enemies_tmp["enemies"]["enemy"]
		
			for e in enemies_list:
				self.enemies.append(Enemy(e["name"], int(e["health"]), int(e["strength"]), e["description"]))
		
		if iniciar_o_cargar == 2: #Cargar partida desde el punto en el que estaba
			xml_file = open("enemiesGuardados.xml", "r")
			enemies_tmp = xmltodict.parse(xml_file.read())
			enemies_list = enemies_tmp["enemies"]["enemy"]

			for e in enemies_list:
				self.enemies.append(Enemy(e["name"], int(e["health"]), int(e["strength"]), e["description"]))
		
	def loadWithJson(self, iniciar_o_cargar): #Tratar datos con JSON
		self.enemies = []
		
		if iniciar_o_cargar == 1: #Iniciar partida desde zero
			with open("enemies.json", "r") as json_file:
				enemies_data = json.load(json_file)
				enemies_list = enemies_data["enemies"]["enemy"]

			for e in enemies_list:
				self.enemies.append(Enemy(e["name"], int(e["health"]), int(e["strength"]), e["description"]))
		if iniciar_o_cargar == 2: #Cargar partida desde el punto en el que estaba
			with open("enemiesGuardados.json", "r") as json_file:
				enemies_data = json.load(json_file)
				enemies_list = enemies_data["enemies"]["enemy"]

			for e in enemies_list:
				self.enemies.append(Enemy(e["name"], int(e["health"]), int(e["strength"]), e["description"]))

	def write_info_xml (self): #Escribir / Guardar en un archivo en formato XML los enemies
		
		enemiesXml = []

		for e in self.enemies:
			enemy_export = {
				"name": e.name,
				"strength": e.strength,
				"health": e.health,
				"description": e.description
			}
		
			enemiesXml.append(enemy_export)
		
		xml_data = {"enemies": {"enemy": enemiesXml}}
		xml_content = xmltodict.unparse(xml_data, pretty=True)
		
		with open ("enemiesGuardados.xml", "w") as xml_file:
			xml_file.write(xml_content)

	def write_info_json (self): #Escribir / Guardar en un archivo en formato JSON los enemies

		enemiesJson = []

		for e in self.enemies:
			enemy_export = {
				"name": e.name,
				"strength": e.strength,
				"health": e.health,
				"description": e.description
			}
				
			enemiesJson.append(enemy_export)

		json_data = {"enemies": {"enemy": enemiesJson}}

		with open("enemiesGuardados.json", "w") as json_file:
			json.dump(json_data, json_file, indent = 4) #indent 4 es para que se lea mejor en el archivo json
