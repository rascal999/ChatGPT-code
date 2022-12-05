#!/usr/bin/env python3

import random

# define a list of possible answers
answers = ["yes", "no", "maybe"]

# ask the player to ask a yes/no question
question = input("Ask me a yes/no question: ")

# choose a random answer from the list
answer = random.choice(answers)

# print the answer to the player's question
print(answer)
