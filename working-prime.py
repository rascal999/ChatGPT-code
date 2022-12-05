#!/usr/bin/env python3

import math

def is_prime(n):
  # Check for small prime numbers
  if n in (2, 3, 5, 7):
    return True

  # Check for even numbers
  if n % 2 == 0:
    return False

  # Check for other factors
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False

  return True

def nth_prime(n):
  if n < 1:
    return None

  primes_found = 0
  current_number = 1

  while True:
    current_number += 1

    if is_prime(current_number):
      primes_found += 1

      if primes_found == n:
        return current_number

# Find the 10th prime number
n = 10
result = nth_prime(n)

print(f"The {n}th prime number is {result}")
