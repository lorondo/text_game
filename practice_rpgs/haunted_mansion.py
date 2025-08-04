### print welcome message
print("Welcome to the Haunted Mansion!")
print("You are distant family memeber of a rich millionaire who has just passed away, leaving this mansion to you.")
print("You decide to pay a visit to the mansion.")
print("The house is dated, creaky, and falling apart. You walk in the front door.")
print("Do you want to enter the living room or the dining room?")

### prompt the user for a choice
roomChoice = input("> ")

if(roomChoice == "living room"):
  print("You enter the living room.")
  print("You see a sleeping pitbull guarding some gold jewelry.")
  print("Do you want to steal the jewelry from the pitbull?")

  pitBullChoice = input("> ")

  if(pitBullChoice == "yes"):
    print("You attempt to steal the jewelry, but it wakes up and rips you to shreds.")
    print("You are now dead.")
  elif(pitBullChoice == "no"):
    print("You decide to not steal the dog's jewelry.")
    print("You turn around and leave the house safely.")
  else:
    print("Invalid choice. Please eneter the yes or no.")

elif(roomChoice == "dining room"):
  print("You enter the dining room.")
  print("You see a shiny vase on the table.")
  print("Do you want to look inside the vase?")

  vaseChoice = input("> ")

  if(vaseChoice == "yes"):
    print("You look inside the vase, it is full of human bones.")
    print("You are now dead.")
  elif(vaseChoice == "no"):
    print("You decide to not look inside the vase.")
    print("You turn around and leave the house.")
  else:
    print("Invalid choice. Please eneter the yes or no.")

else:
  print("Invalid choice. Please eneter the living room or dining room.")