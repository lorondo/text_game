import os

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

currentRoom = "Hall"

rooms = {
  "Garden": {
    "north": "Dining Room",
    "item": "chainsaw"
  },
  "Dining Room": {
    "south": "Garden",
    "west": "Hall",
    "item": "potion"
  },
  "Hall": {
    "south": "Kitchen", # when you're in the Hall, the value of south is Kitchen
    "east": "Dining Room",
    "item": "key"
  },
  "Kitchen": {
    "north": "Hall", # when you're in the Kitchen, the value of north is Hall
    "item": "monster"
  } 
}

showInstructions()

while True:

  status()

  move = input(">") # "get sword", "go north"
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

  # move[0] -> "go"
  if move[0] == "go":
    if move[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][move[1]]
      print(f"You are now in the {currentRoom}!") 
    else: 
      print(f"You can't go {move[1]}!")
  
  # victory condition 1: escaping the house through the garden!
  if "key" in inventory and "potion" in inventory and currentRoom == "Garden":
    print("Through the garden, you escape from the mansion with the magic key and potion!")
    break # ends while loop

  # loss condition: getting eaten by the monster!
  if "item" in rooms[currentRoom] and rooms[currentRoom]["item"] == "monster":
    # victory condition 2: vanquishing the monster!
    if "chainsaw" in inventory:
      print("You defeat the monster with the chainsaw! YOU WIN!")
      break
    else:
      print("You have been eaten!")
      print("GAME OVER!")
      break

