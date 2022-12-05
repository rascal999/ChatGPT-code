#!/usr/bin/env python3

import random

# list of play options
options = ["rock", "paper", "scissors"]

# initialize player and computer scores
player_score = 0
computer_score = 0

# initialize number of rounds
rounds = 3

# play `rounds` number of rounds
for i in range(rounds):
    # get player's play
    player = input("Enter your play (rock, paper, or scissors): ")

    # get computer's play
    computer = random.choice(options)

    # determine the winner of this round
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        player_score += 1
        print("You win this round!")
    elif player == "paper" and computer == "rock":
        player_score += 1
        print("You win this round!")
    elif player == "scissors" and computer == "paper":
        player_score += 1
        print("You win this round!")
    else:
        computer_score += 1
        print("The computer wins this round.")

    # print the current score
    print("The current score is: Player - {} | Computer - {}".format(player_score, computer_score))

# determine the overall winner
if player_score > computer_score:
    print("Congratulations, you won the game!")
elif player_score == computer_score:
    print("The game ended in a tie!")
else:
    print("Sorry, the computer won the game.")
