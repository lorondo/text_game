inventory = []

currentRoom = "Hall"

rooms = {
  "Hall": {
    "south": "Kitchen" ## when you're in the Hall, the value of south is Kitchen
  },
  "Kitchen": {
    "north": "Hall" ## when you're in the Kitchen, the value of north is Hall
  } 
}

print("I am in the", currentRoom)

directions = rooms[currentRoom]

currentRoom = directions

print("I am NOW in the", currentRoom)