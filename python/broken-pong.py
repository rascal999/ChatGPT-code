#!/usr/bin/env python3

import pygame

###
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
###

# initialize the pygame library
pygame.init()

# define the screen dimensions
w, h = 600, 400

# create a screen with the defined dimensions
s = pygame.display.set_mode((w, h))

# define the colors
b = (0, 0, 0)
w = (255, 255, 255)

# define the ball's initial position and speed
x, y = w[0] / 2, h[0] / 2
dx, dy = 4, 4

# define the player's initial position and speed
px, py = 20, h / 2
ps = 5

# define the computer's initial position and speed
cx, cy = w - 20, h / 2
cs = 4

# define the ball's radius
r = 10

# define the player and computer's paddle dimensions
pw, ph = 10, 50

# define the main game loop
while True:
    # fill the screen with the black color
    s.fill(b)

    # check if the player has quit the game
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

    # check if the player has pressed a key to move the paddle
    k = pygame.key.get_pressed()
    if k[pygame.K_UP]:
        py -= ps
    if k[pygame.K_DOWN]:
        py += ps

    # move the computer's paddle towards the ball
    if y < cy:
        cy -= cs
    if y > cy:
        cy += cs

    # check if the ball has hit the top or bottom of the screen
    if y + r >= h or y - r <= 0:
        dy *= -1

    # check if the ball has hit the player's or computer's paddle
    if x - r <= px + pw and y >= py and y <= py + ph:
        dx *= -1
    if x + r >= cx and y >= cy and y <= cy + ph:
        dx *= -1

    # move the ball
    x += dx
    y += dy

    # draw the ball on the screen
    pygame.draw.circle(s, w, (int(x), int(y)), r)

    # draw the player's and computer's paddles on the screen
    pygame.draw.rect(s, w, (px, py, pw, ph))
    pygame.draw.rect(s, w, (cx, cy, pw, ph))

    # update the screen
    pygame.display.flip()
