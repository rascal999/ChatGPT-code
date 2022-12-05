#!/usr/bin/env python3

import curses
import time
import random

# define the initial position and direction of the snake
snake = [(0, 0), (0, 1), (0, 2)]
direction = (0, 1)

# initialize the screen
screen = curses.initscr()
curses.curs_set(0)

# define the boundaries of the game area
min_x = 0
max_x = screen.getmaxyx()[1] - 1
min_y = 0
max_y = screen.getmaxyx()[0] - 1

# define the initial position of the food
food = (random.randint(min_y, max_y), random.randint(min_x, max_x))

# define the main game loop
while True:
    # check if the snake has hit a wall or itself
    if snake[0][0] == min_y or snake[0][0] == max_y or snake[0][1] == min_x or snake[0][1] == max_x or snake[0] in snake[1:]:
        break

    # move the snake in the current direction
    snake.insert(0, (snake[0][0] + direction[0], snake[0][1] + direction[1]))

    # check if the snake has eaten the food
    if snake[0] == food:
        # if it has, generate new food at a random location
        food = (random.randint(min_y, max_y), random.randint(min_x, max_x))
    else:
        # if it hasn't, remove the tail of the snake
        snake.pop()

    # clear the screen
    screen.clear()

    # draw the snake and the food on the screen
    screen.addch(food[0], food[1], "*")
    for y, x in snake:
        screen.addch(y, x, "#")

    # refresh the screen
    screen.refresh()

    # wait for a short time
    time.sleep(0.1)

    # check if the player has pressed a key to change the direction of the snake
    c = screen.getch()
    if c == curses.KEY_UP:
        direction = (-1, 0)
    elif c == curses.KEY_DOWN:
        direction = (1, 0)
    elif c == curses.KEY_LEFT:
        direction = (0, -1)
    elif c == curses.KEY_RIGHT:
        direction = (0, 1)

# clean up and exit
curses.endwin()
