#!/usr/bin/env python3

# Import the random and string modules
import random
import string

# Define a function that generates a random password
def generate_password():
    # Generate a random string of lowercase letters, uppercase letters, and digits
    password = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=12))

    # Return the generated password
    return password

# Call the generate_password() function 10 times to generate 10 random passwords
for i in range(10):
    print(generate_password())
