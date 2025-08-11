def showInstructions():
  #print a main menu and the commands
  print('''
    RPG Game
    ========
    Commands:
        go [direction] (example: go north)
        get [item]
      ''')

inventory = []

currentRoom = "Kitchen"

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
    "south": "Kitchen" # when you're in the Hall, the value of south is Kitchen
    "item": "key"
  },
  "Kitchen": {
    "north": "Hall", # when you're in the Kitchen, the value of north is Hall
    "item": "monster"
  } 
}

showInstructions()

while True:
  print(f"You are in the {currentRoom}!")

  move = input(">") # "get sword", "go north"
  move = move.split(" ", 1) # "get sword" -> ["get", "sword"]
  
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

  

