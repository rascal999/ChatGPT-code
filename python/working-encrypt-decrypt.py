#!/usr/bin/env python3

from cryptography.fernet import Fernet

# Define the secret key
key = b"QQ1-z7BcYb3qKjlnTQ2BHV7hRLkDgJt7pKs4s4V7M8s="

# Create a Fernet instance
fernet = Fernet(key)

# Ask the user for input
mode = input("Enter 'e' to encrypt or 'd' to decrypt: ")
data = input("Enter the data to encrypt or decrypt: ")

# Encrypt or decrypt the data
if mode == "e":
  encrypted_data = fernet.encrypt(data.encode())
  print(f"Encrypted data: {encrypted_data.decode()}")
elif mode == "d":
  decrypted_data = fernet.decrypt(data.encode())
  print(f"Decrypted data: {decrypted_data.decode()}")
else:
  print("Invalid mode.")
