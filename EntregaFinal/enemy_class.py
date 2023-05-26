#!/usr/bin/python3
import random

class Enemy: 

	def __init__ (self, name, health, strength, description = ""):
		
		#Inicializamos el constructor de Enemy
		self.name = name
		self.health = health
		self.strength = strength
		self.description = description

	def set_health (self, health):
		self.health = health

	def get_health (self):
		return self.health
	
	def hurt (self, _atackPlayerTurn):
		self.set_health(self.get_health() - _atackPlayerTurn)

	def set_strength (self):
		self.strength = strength

	def get_strength (self):
		return self.strength

	def atack (self):
		return random.randint(0, self.strength)

	def isDeath (self):
		return (self.get_health() <= 0)
		
	def show_info (self):
		print("__________DATOS ENEMY___________")
		print("Name: " + self.name)
		print("Health: " + str(self.health))
		print("Strength: Between 0 - " + str(self.strength))
		if self.description != "":
			print("Description: " + self.description)
