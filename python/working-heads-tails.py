#!/usr/bin/env python3

import random

# define a list of possible outcomes
outcomes = ["heads", "tails"]

# choose a random outcome
outcome = random.choice(outcomes)

# ask the player to guess the outcome
guess = input("Heads or tails? ")

# check if the player's guess is correct
if guess.lower() == outcome:
    print("You win!")
else:
    print("You lose!")
