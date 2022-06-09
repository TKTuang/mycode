#!/usr/bin/env python3

"""Rock, Paper, Scissor, Gun"""

import random
    
#create list of pick from
my_list = [ "Rock", "Paper", "Scissor", "Gun" ]


while True:
    # ask user for input
    user = input("Rock, Paper, Scissor, Gun SHOOT:  ")
    player1 = random.choice(my_list)
    player2 = random.choice(my_list)

    print(f"\nPlayer 1: {player1}\n\nPlayer 2: {player2}\n\nYou: {user}\n")

    if user == player1 == player2:
        print(f"All players chose {user}.")
        

    #conditions where user wins
    elif user == "Rock" and player1 == "Scissor" and player2 == "Scissor":
        print("Rock smashes scissors! You win!")
    elif user == "Paper" and player1 == "Rock" and player2 == "Rock":
        print("Paper beats rocks! You win!")
    elif user == "Scissor" and player1 == "Paper" and player2 == "Paper":
        print("Scissor cuts papers! You win!")


    #conditions where player1 wins
    elif player1 == "Rock" and user == "Scissor" and player2 == "Scissor":
        print("Rock smashes scissors! Player 1 win!")
    elif player1 == "Paper" and user == "Rock" and player2 == "Rock":
        print("Paper beats rocks! Player 1 win!")
    elif player1 == "Scissor" and user == "Paper" and player2 == "Paper":
        print("Scissor cuts papers! Player 1 win!")

    #conditions where player2 wins
    elif player2 == "Rock" and user == "Scissor" and player1 == "Scissor":
        print("Rock smashes scissors! Player 2 win!")
    elif player2 == "Paper" and user == "Rock" and player1 == "Rock":
        print("Paper beats rocks! Player 2 win!")
    elif player2 == "Scissor" and user == "Paper" and player1 == "Paper":
        print("Scissor cuts papers! Player 2 win!")
    

    #conditions where user lose
    elif user == "Paper" and user == "Scissor" and player1 == "Scissor":
        print("Scissor cuts paper! Player 2 lose!")
        user = input("Rock, Paper, Scissor, Gun SHOOT:  ")
        player1 = random.choice(my_list)
    elif user == "Scissor" and user == "Rock" and player1 == "Rock":
        print("Rock beats scissor! Player 2 lose!")
    elif user == "Rock" and user == "Paper" and player1 == "Paper":
        print("Paper beats rock! You lose!")


    #conditions where player1 lose
    elif player1 == "Paper" and user == "Scissor" and player1 == "Scissor":
        print("Scissor cuts paper! Player 1 lose!")
    elif player1 == "Scissor" and user == "Rock" and player1 == "Rock":
        print("Rock beats scissor! Player 1 los2!")
    elif player1 == "Rock" and user == "Paper" and player1 == "Paper":
        print("Paper beats rock! Player 1 lose!")


    #conditions where player2 lose
    elif player2 == "Paper" and user == "Scissor" and player1 == "Scissor":
        print("Scissor cuts paper! Player 2 lose!")
    elif player2 == "Scissor" and user == "Rock" and player1 == "Rock":
        print("Rock beats scissor! Player 2 lose!")
    elif player2 == "Rock" and user == "Paper" and player1 == "Paper":
        print("Paper beats rock! Player 2 lose!")


    #Gun conditions
    elif user == "Gun" and player1 == "Gun":
        print("Player 1 and You shot each other. Player 2 Wins!")
    elif user == "Gun" and player2 == "Gun":
        print("Player 2 and You shot each other. Player 1 Wins!")
    elif player2 == "Gun" and player1 == "Gun":
        print("Player 2 and Player 1 shot each other. You Wins!")
    elif user == "Gun":
        print("GUN RULES. YOU  WINS")
    elif player1 == "Gun":
        print("GUN RULES. PLAYER 1 WINS")
    elif player2 == "Gun":
        print("GUN RULES. PLAYER 2 WINS")
    else:
        print("No one won")

    answer= input("Do you want to play again? (y/n): ")
    if answer.lower() != "y": # if the user answers no,
        break # the while loop breaks and the game ends
