inventory = []

currentRoom = "Hall"

rooms = {
  "Hall": {
    "south": "Kitchen" # when you're in the Hall, the value of south is Kitchen
  },
  "Kitchen": {
    "north": "Hall", # when you're in the Kitchen, the value of north is Hall
    "item": "chainsaw"
  } 
}

while True:
  move = input(">") # "get sword", "go north"
  move = move.split(" ", 1) # "get sword" -> ["get", "sword"]
  # move[0] -> "get"
  if move[0] == "get":
    if move[1] == rooms[currentRoom]["item"]:
  

