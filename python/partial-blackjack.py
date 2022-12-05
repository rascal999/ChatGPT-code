#!/usr/bin/env python3

import random

# define the ranks and suits of the cards
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♠", "♥", "♣", "♦"]

# define the player's and dealer's initial hands
player_hand = []
dealer_hand = []

# define the player's initial score and bet
player_score = 100
player_bet = 0

# define the main game loop
while True:
    # shuffle the deck of cards
    deck = [rank + suit for rank in ranks for suit in suits]
    random.shuffle(deck)

    # reset the player's and dealer's hands
    player_hand = []
    dealer_hand = []

    # ask the player to place their bet
    print("You have $" + str(player_score) + ". How much do you want to bet?")
    player_bet = int(input())

    # check if the player has enough money to place the bet
    if player_bet > player_score:
        print("You do not have enough money to place that bet. Please try again.")
        continue

    # deal two cards to the player and the dealer
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    # show the player's hand and the dealer's top card
    print("Your hand: " + ", ".join(player_hand))
    print("Dealer's hand: " + dealer_hand[0])

    # check if the player has blackjack (21 points)
    if sum([ranks.index(card[0]) + 1 for card in player_hand]) == 21:
        print("You have blackjack! You win!")
