#!/usr/bin/env python3

import random

# define the minimum and maximum number
min_num = 1
max_num = 10

# choose a random number between the minimum and maximum
target = random.randint(min_num, max_num)

# ask the player to guess the number
guess = int(input(f"Guess a number between {min_num} and {max_num}: "))

# check if the player's guess is correct
if guess == target:
    print("You win!")
else:
    print("You lose!")
