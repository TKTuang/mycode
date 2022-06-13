#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live


import random
from pprint import pprint

#Function to call when encountering a monster to fight
def battle():

    playerHealth = 25
    monsterHealth = 20
    elitemonsterHealth = 30

    #skill/attack list
    attacks = [{"healing" : 3}, {"block" : 0}, {"hit" : 3}, {"critDamage" : 5}]


    #loops until either player OR monster Health <= 0
    while playerHealth >= 0 or monsterHealth >= 0:
        print('''
=================
Entering Battle:
----------------- ''')
        print(f"You health is: {playerHealth}")
        print(f"The monster health is: {monsterHealth}")
        pickSkill = input("Choose an attack (1, 2, 3, or 4): ")
        userSkill = ""
        if pickSkill == "1":
            userSkill == attacks[0]
            playerHealth -= attacks[0]["healing"]
            print(playerHealth)
        elif pickSkill == "2":
            userSkill == attacks[1]
            playerHealth -= attacks[1]["block"] 
            print(playerHealth)
        elif pickSkill == "3":
            monsterHealth -= attacks[2]["hit"] 
            print(monsterHealth)
        elif pickSkill == "4":
            monsterHealth -= attacks[3]["critDamage"] 
            print(monsterHealth)
        else:
            print("You donot have that skill.")
        enemySkill = random.choice(attacks) 
        print(enemySkill)

        if enemySkill == attacks[0]:
            monsterHealth -= attacks[0]["healing"]
            print(monsterHealth)
        elif enemySkill == attacks[1]:
            monsterHealth -= attacks[1]["block"]
            print(monsterHealth)         
        elif enemySkill == attacks[2]:
            playerHealth -= attacks[2]["hit"]
            print(playerHealth)
        elif enemySkill == attack[3]:
            playerHealth -= attacks[3]["critDamage"]
            print(playerHealth)

battle()

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
--------
Objective: Find the lost Guardian.
Save him with your potion and a key.
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
    print('You found a '  + rooms[currentRoom]['item'])
  if "npc" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['npc'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []


#list of NPCs
npcs = random.choice(["guardian", "cat", "dog", "monster", "elite monster"])

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Entrance' : {
                  'north' : 'Main Room'
                },

            'Main Room' : {
                  'north' : 'Hall of Secrets',
                  'west' : 'Weapon Room',
                  'east' : 'Library',
                  'south' : 'Entrance',
                  'item' : '',
                  'npc'  : 'guardian'
                },
            'Hall of Secrets' : {
                  'south' : 'Main Room',
                  'item' : '',
                  'npc' : npcs
               },
            'Weapon Room' : {
                  'west' : 'Basement',
                  'east' : 'Main Room',
                  'npc' : 'cat',
                  'item' : ''
               },
            'Library' : {
                  'north' : 'Second Floor',
                  'east' : 'Magic Room',
                  'west' : 'Main Room',
                  'npc' : npcs,
                  'item' : ''
               },
            'Magic Room' : {
                 'west' : 'Library',
                 'npc' : npcs,
                 'item' : ''
              },
            'Second Floor' : {
                'south' : 'Library',
                'npc' : npcs,
                'item' : ''
              },
            'Basement' : {
                'east' : 'Weapon Room',
                'npc' : npcs,
                'item' : ''
            }
         }

#start the player from Entrance
currentRoom = 'Entrance'

# create a list of your rooms
roomlist= list(rooms.keys())

# items to distribute
items= ["guardian blade","cake","key","potion", "apple", "carrot", "strength buff", "socks"]

# randomize the order
random.shuffle(roomlist)

for x in range(8): # there are 4 rooms, so this must be 4

    roomselect= roomlist[x]
    itemselect= items[x]
    rooms[roomselect]["item"] = itemselect
    print(rooms[roomselect]["item"])
                                             


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


  #if they type 'get' first
    if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
            inventory += [move[1]]
      #display a helpful message
            print('You picked up the ', move[1] + '.')
      #delete the item from the room
            del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
        else:
      #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')


  ## If a player enters a room with a monster with a weapon  
    if 'npc' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['npc'] and 'guardian blade' in inventory and 'potion' in inventory:
        showStatus()
        print("You killed the monster with your Guardian Blade!!!")
        del rooms[currentRoom]['npc']
        break
    elif  'npc' in rooms[currentRoom] and 'elite monster' in rooms[currentRoom]['npc'] and 'strength buff' in inventory and 'guardian blade' in inventory:
        showStatus()
        print("You killed the monster with your strength buff and Guardian Blade!!!")
        del rooms[currentRoon]['npc']
        break

  ## Define how a player can win
    if 'npc' in rooms[currentRoom] and 'guardian' in rooms[currentRoom]['npc'] and 'key' in inventory and 'potion' in inventory:
        print('You found the lost guardian.. YOU WIN!')
        break

#If a player enters a room with a monster with no weapon
    
    if 'npc' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['npc'] and  'guardian blade' not in inventory:
        showStatus()
        print('You encountered a monster and you dont have anything to defend yourself with..GAME OVER!')
        break
    elif 'npc' in rooms[currentRoom] and 'elite monster' in rooms[currentRoom]['npc'] and 'guardian blade' not in inventory and 'strength buff' not in inventory:
        showStatus()
        print("You were murdered by the elite monster")
        break
