#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live


import random
from pprint import pprint

"""#Function to call when encountering a monster to fight
def battle():

    playerHealth = 25
    monsterHealth = 20
    elitemonsterHealth = 30

    #skill/attack list
    attacks = ["healing" , "hit", "critDamage"]
    print('''
========================                                                                                            
Entering Battle: Ready!
------------------------''')

    #loops until either player OR monster Health <= 0
    while True:

        print(f"You health is: {playerHealth}")
        print(f"The monster health is: {monsterHealth}")
        pickSkill = input("Choose a skill (1/2/3/4): ")
        enemySkill = random.choice(attacks)
        print('''
-------------------------------------''')
       #Intense battle commencing atm
        if pickSkill == "1":
            if "potion" in inventory:
                playerHealth += 3
                print("You heal for 3 Health Points")
            else:
                print("You do not have any potion")
        elif pickSkill == "2":
            monsterHealth -= 3
            print("You deal -3 damages to the monster!")
        elif pickSkill == "3":
            if "crit buff" in inventory:
                monsterHealth -= 5
                print("Hits the moster with critical damage of -5!")
            else:
                monsterHealth -= 3
                print("You deal -3 damage")
        else:
            print("You do not have that skill.")
 

        if enemySkill == attacks[0]:
            monsterHealth += 3
            print("Monster heals for +3 Health Points")       
        elif enemySkill == attacks[1]:
            playerHealth -= 3
            print("You took -3 damage")
        elif enemySkill == attacks[2]:
            playerHealth -= 5
            print("You took -5 crit damage!")
        
        if playerHealth <= 0:
            break
        elif monsterHealth <= 0:
            break

battle()"""

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
--------
Objective: Find the lost Guardian.
Save him with a key in your possesion.
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
inventory = ["guardian blade"]


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
items= ["potion","crit buff","","potion", "potion", "key", "crit buff", "crit buff"]

# randomize the order
random.shuffle(roomlist)

for x in range(8): # there are 4 rooms, so this must be 4

    roomselect= roomlist[x]
    itemselect= items[x]
    rooms[roomselect]["item"] = itemselect
    #print(rooms[roomselect]["item"])
                                             


showInstructions()

#Function to call when encountering a monster to fight
def battle():

    playerHealth = 25
    monsterHealth = 20
    elitemonsterHealth = 30

    #skill/attack list
    attacks = ["healing" , "hit", "critDamage"]
    print('''
========================
Entering Battle: Ready!
------------------------''')

    #loops until either player OR monster Health <= 0
    while True:

        print(f"You health is: {playerHealth}")
        print(f"The monster health is: {monsterHealth}")
        showStatus()
        pickSkill = input("Choose a skill (1/2/3/4): ")
        enemySkill = random.choice(attacks)
        print('''
-------------------------------------''')
       #Intense battle commencing atm
        if pickSkill == "1":
            if "potion" in inventory:
                playerHealth += 3
                print("You heal for 3 Health Points")
                inventory.remove("potion")
            else:
                print("You do not have any potion")
        elif pickSkill == "2":
            monsterHealth -= 3
            print("You deal -3 damages to the monster!")
        elif pickSkill == "3":
            if "crit buff" in inventory:
                monsterHealth -= 5
                print("Hits the moster with critical damage of -5!")
                inventory.remove("crit buff")
            else:
                monsterHealth -= 3
                print("You deal -3 damage")
        else:
            print("You do not have that skill.")


        if enemySkill == attacks[0]:
            monsterHealth += 3
            print("Monster heals for +3 Health Points")
        elif enemySkill == attacks[1]:
            playerHealth -= 3
            print("You took -3 damage")
        elif enemySkill == attacks[2]:
            playerHealth -= 5
            print("You took -5 crit damage!")



        if playerHealth <= 0:
            print("You lost to the monster...GAME OVER")
            currentRoom = "Entrance"
            break
        elif monsterHealth <= 0:
            print("Congratulations. Monster defeated.")
            del rooms[currentRoom]['npc']
            break


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
    if 'npc' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['npc']:
        showStatus()
        battle()
    elif  'npc' in rooms[currentRoom] and 'elite monster' in rooms[currentRoom]['npc']:
        showStatus()
        battle()

  ## Define how a player can win
    if 'npc' in rooms[currentRoom] and 'guardian' in rooms[currentRoom]['npc'] and 'key' in inventory:
        print('You found the lost guardian.. YOU WIN!')
        break

#If a player enters a room with a monster with no weapon
    
    if 'npc' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['npc'] and  'guardian blade' not in inventory:
        showStatus()
        print('You encountered a monster and you dont have anything to defend yourself with..GAME OVER!')
        break
    elif 'npc' in rooms[currentRoom] and 'elite monster' in rooms[currentRoom]['npc'] and 'guardian blade' not in inventory:
        showStatus()
        print("You were murdered by the elite monster")
        break
