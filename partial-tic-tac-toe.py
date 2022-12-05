#!/usr/bin/env python3

import itertools

# define the board as a list of lists
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# define the players as a list of tuples
players = [("X", "O")]

# define a function to print the board
def print_board():
    print("\n".join([" ".join(row) for row in board]))

# define a function to check if a player has won
def check_winner(player):
    # check for horizontal wins
    for row in board:
        if row == [player, player, player]:
            return True
    # check for vertical wins
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # check for diagonal wins
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# define a function to check if the game is a draw
def check_draw():
    # check if there are any empty spaces on the board
    for row in board:
        if " " in row:
            return False
    return True

# define a function to get the player's move
def get_move(player):
    # get the player's row and column input
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1
    # make sure the space is empty
    if board[row][col] != " ":
        print("This space is already taken. Please try again.")
        get_move(player)
    else:
        # update the board with the player's move
        board[row][col] = player

# define the main game loop
for player, opponent in itertools.cycle(players):
    print_board()
    print(f"Player {player}, it's your turn.")
    get_move(player)
    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break
    if check_draw():
        print_board()
        print("The game is a draw.")
        break
