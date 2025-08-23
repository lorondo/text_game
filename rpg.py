import random
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.attack = 5
        self.defense = 0
    
    def is_alive(self):
        return self.health > 0
    
    def print_status(self):
        print(f"{self.name}: Health = {self.health}, Attack = {self.attack}, Defense = {self.defense}, Treasure = {self.treasure}")

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage

    def print_status(self):
        print(f"{self.name}: Health = {self.health}, Attack = {self.attack}, Defense = {self.defense}")

def battle(player, enemy):
    print("A fierce", enemy.name, "attacks!")
    while player.is_alive() and enemy.is_alive():
        print("\n" + "-" * 20)
        player.print_status()
        enemy.print_status()
        print("-" * 20 + "\n")

        player_damage = max(0, player.attack)
        enemy.take_damage(player_damage)
        print(f"You hit the {enemy.name} for {player_damage} damage.")

        if enemy.is_alive():
            enemy_damage = max(0, enemy.attack - player.defense)
            player.health -= enemy_damage
            print(f"The {enemy.name} strikes you for {enemy_damage} damage.")

    if player.is_alive():
        print("\nVictory! You have defeated the", enemy.name + "!")

    else:
        print("\nYou have been slain by the", enemy.name + "!")
        print("Game Over")

def showInstructions():
  #print a main menu and the commands
  print('''
    RPG Game
    ========
    Commands:
        go [direction] (example: go north)
        get [item]
      ''')

def status():
  print("--------------")
  print(f"Current Room: {currentRoom}")
  print(f"Inventory: {inventory}")

  if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]:
    room_item = rooms[currentRoom]["item"]
    print(f"You see a {room_item}!")

  print("--------------")

inventory = []

currentRoom = "Dungeon Room 1"

rooms = {
    # Beginning Dungeon
    "Dungeon Room 1": {
        "door": "Dungeon Hub"
    },
    "Dungeon Room 2": {
        "door": "Dungeon Hub"
    },
    "Dungeon Room 3": {
        "door": "Dungeon Hub"
    },
    "Dungeon Room 4": {
        "door": "Dungeon Hub"
    },
    "Dungeon Room 5": {
        "door": "Dungeon Hub"
    },
    "Dungeon Hub": {
        "door 1": "Dungeon Room 1",
        "door 2": "Dungeon Room 2",
        "door 3": "Dungeon Room 3",
        "door 4": "Dungeon Room 4",
        "door 5": "Dungeon Room 5",
    }
}