# import random
import os

# player stats
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.attack = 1
        self.defense = 0
    
    def is_alive(self):
        return self.health > 0
    
    def print_status(self):
        print(f"{self.name}: Health = {self.health}, Attack = {self.attack}, Defense = {self.defense}")

# item stats
class Equipment:
   def __init__(self, name, health_bonus, attack_bonus, defense_bonus):
      self.name = name
      self.health_bonus = health_bonus
      self.attack_bonus = attack_bonus
      self.defense_bonus = defense_bonus

# function to adjust the player stats with item bonuses
def equip(player, equipment):
    print("You equip", equipment.name, "!")
    equipped_gear.append(equipment)
    rooms[currentRoom]["equipment"] = ""
    print(equipment)

    #while equipment.name in equipped_gear:
    player.health += equipment.health_bonus
    player.attack += equipment.attack_bonus
    player.defense += equipment.defense_bonus
      
    print("\n" + "-" * 20)
    player.print_status()
    print("-" * 20 + "\n")

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
  print(f"Equipment: {equipped_gear}")

  if "description" in rooms[currentRoom]:
     room_description = rooms[currentRoom]["description"]
     print(room_description)

  if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]:
    room_item = rooms[currentRoom]["item"]
    print(f"You see a {room_item}!")
  
  if "equipment" in rooms[currentRoom] and rooms[currentRoom]["equipment"]:
     room_equipment = rooms[currentRoom]["equipment"]
     equip(player, room_equipment)

  print("--------------")

inventory = []

equipped_gear = []

currentRoom = "Dungeon Room One"

rooms = {
    # Beginning Dungeon
    "Dungeon Room One": {
        "door": "Dungeon Hub",
        "item": "doll",
        "equipment": Equipment("Shield", 0, 0, 3),
        "description": "You are now in Dungeon Room One. There is one door in this room."
    },
    "Dungeon Room Two": {
        "door": "Dungeon Hub",
        "item": "apple pie",
        "equipment": Equipment("Sword", 0, 3, 0),
        "description": "You are now in Dungeon Room Two. There is one door in this room."
    },
    "Dungeon Room Three": {
        "door": "Dungeon Hub",
        "item": "grapes",
        "description": "You are now in Dungeon Room Three. There is one door in this room."
    },
    "Dungeon Hub": {
        "door 1": "Dungeon Room One",
        "door 2": "Dungeon Room Two",
        "door 3": "Dungeon Room Three",
        "item": "banana",
        "description": "You are now in the Dungeon Hub. There are three dungeon doors in this room, each numbered one through three. From here, you can enter door 1, door 2, or door 3."
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

  # move[0] -> "get"; for picking up items
  if move[0] == "get":
    if move[1] == rooms[currentRoom]["item"]:
      print(f"You got a {move[1]}!")
      inventory.append(move[1])
      rooms[currentRoom]["item"] = ""
      print(inventory)
    else:
      print(f"You don't see a {move[1]} here!")

  # move[0] -> "enter"; for entering new rooms through doors and passages
  if move[0] == "enter":
    if move[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][move[1]]
      print(f"You are now in {currentRoom}!") 
    else: 
      print(f"You can't go {move[1]}!")



