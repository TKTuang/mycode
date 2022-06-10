#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

import random

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
--------
Objective: Find the lost Guardian.
Save him with your your potion and a key.
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  if "npc" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['npc'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#List of items
items = ["potion", "key", "cake", "strength buff",]

#list of NPCs
npc = ["guardian", "cat", "dog", "monster", "elite monster"]

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Entrance' : {
                  'north' : 'Main Room'
                },

            'Main Room' : {
                  'north' : 'Hall of Secrest',
                  'west' : 'Weapon Room',
                  'east' : 'Library',
                  'south' : 'Entrance',
                  'npc' : 'dog',
                  'item' : random.choice(items)
                },
            'Hall of Secrets' : {
                  'south' : 'Main Room',
                  'item' : random.choice(items),
                  'npc' : random.choice(npc),
                  'north' : 'Locked Door'
               },
            'Weapon Room' : {
                  'north' : 'Second Floor',
                  'west' : 'Basement',
                  'east' : 'Main Room',
                  'npc' : 'cat',
                  'item' : 'guardian blade'
               },
            'Library' : {
                  'north' : 'Second floor',
                  'east' : 'Basement',
                  'northeast' : 'Magic Room',
                  'npc' : random.choice(npc),
                  'item' : random.choice(items)
               },
            'Magic Room' : {
                 'southwest' : 'Library',
                 'npc' : random.choice(npc),
                 'item' : random.choice(items)
              },
            'Second Floor' : {
                'southwest' : 'Weapon Room',
                'southeast' : 'Library',
                'npc' : random.choice(npc),
                'item' : random.choice(items)
              },
            'Basement' : {
                'east' : 'Weapon Room',
                'west' : 'Library',
                'npc' : random.choice(npc),
                'item' : random.choice(items)
            }
         }

#start the player from Entrance
currentRoom = 'Entrance'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if the type 'pat' first
  if move[0] == 'pat':
      if "npc" in rooms[currentRoom] == 'dog' and move[1] in rooms[currentRoom]['npc']:
          print("Good boy")
      elif "npc" in rooms[currentRoom] == 'cat' and move[1] in rooms[currentRoom]['npc']:
          print("The cat hiss and ran away from you")
      else:
          print("You shouldn't pet that")

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  
  ## If a player enters a room with a monster with a weapon  
    if 'monster' in rooms[currentRoom]['npc'] and 'guardian blade' in inventory:
        print("You killed the monster with your Guardian Blade!!!")
    elif 'elite monster' in room[currentRoom]['npc'] and 'strength buff' in inventory and 'guardian blade' in inventory:
        print("You killed the monster with your strength buff and Guardian Blade!!!")

  ## Define how a player can win
  if 'guardian' in rooms[currentRoom]['item'] and 'key' in inventory and 'potion' in inventory:
    print('You found the lost guardian.. YOU WIN!')
    break

  ## If a player enters a room with a monster with no weapon
  elif 'guardian blade' not in inventory and 'monster' in rooms[currentRoom]['item']:
    print('You encountered a monster and you dont have anything to defend yourself with..GAME OVER!')
    break
