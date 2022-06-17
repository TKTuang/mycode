#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

import crayons
import random
from pprint import pprint


def showInstructions():
    #print a main menu and the commands
    print(crayons.yellow('''
RPG Game
--------
Objective: Find the lost Guardian.
Save him with a key in your possesion.
========
Commands:
  go [direction]
  get [item]
  pat [animal]
'''))

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + crayons.cyan(currentRoom))
    #print the current inventory
    print('Inventory : ' + crayons.blue(str(inventory)))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You found a '  + crayons.red(rooms[currentRoom]['item']))
    if "npc" in rooms[currentRoom]:
        print('You see a ' + crayons.red(rooms[currentRoom]['npc']))
    print("---------------------------")


#an inventory, which is initially empty
inventory = ["guardian blade"]


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
                  'npc'  : ''
                },
            'Hall of Secrets' : {
                  'south' : 'Main Room',
                  'item' : '',
                  'npc' : '',
               },
            'Weapon Room' : {
                  'west' : 'Basement',
                  'east' : 'Main Room',
                  'npc' : '',
                  'item' : ''
               },
            'Library' : {
                  'north' : 'Second Floor',
                  'east' : 'Magic Room',
                  'west' : 'Main Room',
                  'npc' : '',
                  'item' : ''
               },
            'Magic Room' : {
                 'west' : 'Library',
                 'npc' : '',
                 'item' : ''
              },
            'Second Floor' : {
                'south' : 'Library',
                'npc' : '',
                'item' : ''
              },
            'Basement' : {
                'east' : 'Weapon Room',
                'npc' : '',
                'item' : ''
            }
         }

#start the player from Entrance
currentRoom = 'Entrance'

# create a list of your rooms
roomlist= list(rooms.keys())

# items to distribute
items= ["potion","crit buff","potion","potion", "potion", "key", "crit buff", "crit buff"]
#list of NPCs 
npcs = [ "", "cat", "guardian", "monster",  "dog", "monster", "monster", ""]

# randomize the order
random.shuffle(roomlist)

for x in range(8): # there are 4 rooms, so this must be 4

    roomselect= roomlist[x]
    itemselect= items[x]
    rooms[roomselect]["item"] = itemselect
    #print(rooms[roomselect]["item"])
                                             
for y in range(8): # there are 4 rooms, so this must be 4

    roomselect= roomlist[y]
    npcselect= npcs[y]
    rooms[roomselect]["npc"] = npcselect
    #print(rooms[roomselect]["npc"])

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
            print(crayons.magenta('You can\'t go that way!'))


  #if they type 'get' first
    if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
            inventory += [move[1]]
      #display a helpful message
            print('You picked up the ', crayons.red(move[1] + '.'))
      #delete the item from the room
            del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
        else:
      #tell them they can't get it
            print(crayons.magenta('Can\'t get ' + move[1] + '!', bold=True))
    

    #if they type "pat" first
    if move[0] == 'pat':
        if "npc" in rooms[currentRoom] and "dog" in rooms[currentRoom]["npc"]:
            print(crayons.green("Good boy", bold=True))
        elif "npc" in rooms[currentRoom] and "cat" in rooms[currentRoom]["npc"]:
            print(crayons.green("Mewow", bold=True))
        else:
            print(crayons.magenta("You shouldn't have done that..."))


  ## If a player enters a room with a monster with a weapon  
    if 'npc' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['npc']:
        #Function to call when encountering a monster to fight

        playerHealth = 20
        monsterHealth = 20

        #skill/attack list
        attacks = ["healing" , "hit", "critDamage"]
        print(crayons.yellow('''
========================
Entering Battle: Ready!
------------------------'''))

        #loops until either player OR monster Health <= 0
        while True:

            print(f"Your health is: {playerHealth}")
            print(f"The monster health is: {monsterHealth}")
            print(f"Inventory: {inventory}")
            pickSkill = input(crayons.yellow("""Skill: 
1: to heal with potion
2: to attack the monster
3: to attack monster with crit buff: 
Choose a skill (1/2/3): """))
            print("""----------------------------------""")
            enemySkill = random.choice(attacks)
            print('''
-------------------------------------''')
           #Intense battle commencing atm
            if pickSkill == "1":
                if "potion" in inventory:
                    playerHealth += 3
                    print("You heal for " +crayons.green('3 Health Points'))
                    inventory.remove("potion")
                else:
                    print(crayons.magenta("You do not have any potion"))
            elif pickSkill == "2":
                monsterHealth -= 3
                print("You deal " + crayons.red('3 damages to the monster!'))
            elif pickSkill == "3":
                if "crit buff" in inventory:
                    monsterHealth -= 5
                    print("Hits the moster with " + crayons.red('critical damage of 5!'))
                    inventory.remove("crit buff")
                else:
                    monsterHealth -= 3
                    print("You deal " + crayons.red('3 damage'))
            else:
                print(crayons.magenta("You do not have that skill."))

            if enemySkill == attacks[0]:
                monsterHealth += 3
                print("Monster heals for " + crayons.green('3 Health Points'))
            elif enemySkill == attacks[1]:
                playerHealth -= 2
                print("You took " + crayons.red('2 damage'))
            elif enemySkill == attacks[2]:
                playerHealth -= 3
                print("You took " + crayons.red('3 crit damage!'))

            if playerHealth <= 0:
                print(crayons.magenta("You got DEFEATED...respawn at the Entrance", bold=True))
                currentRoom = "Entrance"
                break

            elif monsterHealth <= 0:
                print(crayons.cyan("Congratulations. Monster defeated.", bold=True))
                del rooms[currentRoom]['npc']
                break

  ## Define how a player can win
    if 'npc' in rooms[currentRoom] and 'guardian' in rooms[currentRoom]['npc'] and 'key' in inventory:
        print(crayons.green('You found the lost guardian.. YOU WIN!', bold=True))
        break

