#!/usr/bin/python3

""" Rock Paper Scissor game for multiple-players"""
import random

#create list
powers = ["Paper", "Rock", "Scissor", "Gun"]

#get desired numbers of players
number_players = int(input("How many players are there(1-10): "))

player_power = []
players = 0

#create players and pick their power
while players <= number_players:
    player_power.append(random.choice(powers))
    print(player_power)
    players += 1


#convert list into string
mystring = ''
for x in player_power:
    mystring += ' '+ x
print(mystring)


#
if mystring in "Rock Paper Scissor":
    print("It's a tie")



matches = []
 
for match in player_power:
    if "Gun" in match:
        matches.append(match)
        print(matches)




"""if any("Gun" in word for word in player_power):
    print('\'Gun\' is there inside the list!')
#else:
    print('\'AskPython\' is not there inside the list)"""
