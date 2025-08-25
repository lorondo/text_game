# import random
import os

# player stats
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.attack = 5
        self.defense = 0
    
    def is_alive(self):
        return self.health > 0
    
    def print_status(self):
        print(f"{self.name}: Health = {self.health}, Attack = {self.attack}, Defense = {self.defense}")

# enemy stats
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

# battle function
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
        rooms[currentRoom]["enemy"] = ""

    else:
        print("\nYou have been slain by the", enemy.name + "!")
        print("Game Over")

def showInstructions():
  #print a main menu and the commands
  print('''
    RPG Game
    ========
    Commands:
        enter [destination] (example: enter door 1)
        get [item]
      ''')

def status():
  print("--------------")
  print(f"Current Room: {currentRoom}")
  print(f"Inventory: {inventory}")

  if "description" in rooms[currentRoom]:
     room_description = rooms[currentRoom]["description"]
     print(room_description)

  if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]:
    room_item = rooms[currentRoom]["item"]
    print(f"You see a {room_item}!")

  if "enemy" in rooms[currentRoom] and rooms[currentRoom]["enemy"]:
     room_enemy = rooms[currentRoom]["enemy"]
     battle(player, room_enemy)

  print("--------------")

inventory = []

currentRoom = "Dungeon Room One"

rooms = {
    # Beginning Dungeon
    "Dungeon Room One": {
        "door": "Dungeon Hub",
        "item": "key",
        "description": "You are now in Dungeon Room One. There is one door in this room."
    },
    "Dungeon Room Two": {
        "door": "Dungeon Hub",
        "item": "cake",
        "description": "You are now in Dungeon Room Two. There is one door in this room."
    },
    "Dungeon Room Three": {
        "door": "Dungeon Hub",
        "item": "grapes",
        "description": "You are now in Dungeon Room Three. There is one door in this room."
    },
    "Dungeon Room Four": {
        "door": "Dungeon Hub",
        "item": "orange",
        "description": "You are now in Dungeon Room Four. There is one door in this room."
    },
    "Dungeon Room Five": {
        "door": "Dungeon Hub",
        "item": "apple",
        "description": "You are now in Dungeon Room Five. There is one door in this room.",
        "enemy" : Enemy("Werewolf", 5, 1, 1)
    },
    "Dungeon Hub": {
        "door 1": "Dungeon Room One",
        "door 2": "Dungeon Room Two",
        "door 3": "Dungeon Room Three",
        "door 4": "Dungeon Room Four",
        "door 5": "Dungeon Room Five",
        "item": "banana",
        "description": "You are now in the Dungeon Hub. There are five dungeon doors in this room, each numbered one through five. From here, you can enter door 1, door 2, door 3, door 4, or door 5."
    }
}

showInstructions()

player_name = input("Enter your name: ")
player = Player(player_name)

while player.is_alive():

  status()

  move = input(">") # "get sword", "enter door one"
  move = move.split(" ", 1) # "get sword" -> ["get", "sword"]
  
  os.system("cls")

  # move[0] -> "get"
  if move[0] == "get":
    if move[1] == rooms[currentRoom]["item"]:
      print(f"You got a {move[1]}!")
      inventory.append(move[1])
      rooms[currentRoom]["item"] = ""
      print(inventory)
    else:
      print(f"You don't see a {move[1]} here!")

  # move[0] -> "enter"
  if move[0] == "enter":
    if move[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][move[1]]
      print(f"You are now in {currentRoom}!") 
    else: 
      print(f"You can't go {move[1]}!")
