#!/usr/bin/env python3

# define a greeting message
greeting = "Hello! I'm a simple chat bot. What's your name?"

# print the greeting message
print(greeting)

# receive the user's name
name = input()

# respond to the user's name
response = "Nice to meet you, {}! How can I help you today?".format(name)

# print the response
print(response)
