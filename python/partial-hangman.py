#!/usr/bin/env python3

import random

# define the word list
words = ["apple", "banana", "orange", "strawberry", "grape"]

# choose a random word from the list
word = random.choice(words)

# define the number of incorrect guesses allowed
max_guesses = 6

# define a list to store the letters the player has guessed
guesses = []

# define a function to print the hangman diagram
def print_hangman(guesses):
    # define the parts of the hangman diagram
    parts = ["""
        +---+
        |   |
            |
            |
            |
            |
        =========
        """,
    """
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
    """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
    """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
    """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        """,
    """
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        """,
    """
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        """]

    # print the appropriate part of the hangman diagram
    print(parts[len(guesses)])

# define a function to check if the player has won
def check_win(word, guesses):
    # check if all the letters in the word have been guessed
    for letter in word:
        if letter not in guesses:
            return False
    return True

# define a function to check if the player has lost
def check_loss(guesses, max_guesses):
    # check if the player has exceeded the maximum number of incorrect guesses
    if len(guesses) >= max_guesses:
        return True
    return False

# define the main game loop
while True:
    # print the hangman diagram
    print_hangman(guesses)

    # print the current state of the word, showing only the letters the player has guessed
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\n")

    # get the player's next guess
    guess = input("Enter your next guess: ")

    # add the guess to the list of guesses
    guesses.append(guess)

    # check if the player has won or lost
    if check_win(word, guesses):
        print("You win!")
        break
    if check_loss(guesses, max_guesses):
        print("You lose!")
        break
