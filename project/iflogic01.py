#!/usr/bin/env python3

"""Rock, Paper, Scissor, Gun"""

import random

#create list of pick from
my_list = [ "Rock", "Paper", "Scissor", "Gun" ]

# ask user for input
user = input("Rock, Paper, Scissor, Gun SHOOT:  ")
player1 = random.choice(my_list)
player2 = random.choice(my_list)


#conditions where user wins
if user == "Gun":
    print(f"Guns RULES. YOU WIN!")
elif user == "Rock" and player1 == "Scissor" and player2 == "Scissor":
    print("Rock smashes scissors! You win!")
elif user == "Paper" and player1 == "Rock" and player2 == "Rock":
    print("Paper beats rocks! You win!")
elif user == "Scissor" and player1 == "Paper" and player2 == "Paper":
    print("Scissor cuts papers! You win!")


#conditions where player1 wins
if player1 == "Gun":
    print(f"Guns RULES. PLAYER 1 WIN!")
elif player1 == "Rock" and user == "Scissor" and player2 == "Scissor":
    print("Rock smashes scissors! Player 1 win!")
elif player1 == "Paper" and user == "Rock" and player2 == "Rock":
    print("Paper beats rocks! Player 1 win!")
elif player1 == "Scissor" and user == "Paper" and player2 == "Paper":
    print("Scissor cuts papers! Player 1 win!")

#conditions where player2 wins
if player2 == "Gun":
    print(f"Guns RULES. PLAYER 2 WIN!")
elif player2 == "Rock" and user == "Scissor" and player1 == "Scissor":
    print("Rock smashes scissors! Player 2 win!")
elif player2 == "Paper" and user == "Rock" and player1 == "Rock":
    print("Paper beats rocks! Player 2 win!")
elif player2 == "Scissor" and user == "Paper" and player1 == "Paper":
    print("Scissor cuts papers! Player 2 win!")

#print(f"\nPlayer 1: {player1}\n\nPlayer 2: {player2}\n\nYou: {user}\n")




