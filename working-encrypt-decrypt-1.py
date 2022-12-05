#!/usr/bin/env python3

### Added manually to make script work
import base64
###

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Ask the user for the password
password = input("Enter the password: ")

# Generate a key from the password using PBKDF2
salt = b"salt"
kdf = PBKDF2HMAC(
  algorithm=hashes.SHA256(),
  length=32,
  salt=salt,
  iterations=100000
)
key = base64.urlsafe_b64encode(kdf.derive(password.encode()))

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
