#!/usr/bin/env python3

import hashlib

# Ask the user for input
data = input("Enter the data to hash: ")

# Calculate the SHA-256 hash of the data
hash = hashlib.sha256(data.encode()).hexdigest()

# Ask the user for the hash to verify
verify = input("Enter the hash to verify: ")

# Check if the entered hash matches the calculated hash
if verify == hash:
  print("The entered hash matches the calculated hash.")
else:
  print("The entered hash does not match the calculated hash.")
