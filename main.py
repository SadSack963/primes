# Sieve of Eratosthenes
# =====================

# My thanks to Geeks for Geeks for the original implementation of the sieve algorithm
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

# Python program to generate all primes <= a given number using the Sieve of Eratosthenes

from sieve import sieve_of_eratosthenes

# Start
if __name__ == '__main__':
    print("Sieve of Eratosthenes\n"
          "=====================")
    limit = int(input("Find all primes up to : "))

    # print(f"List of primes: {sieve_of_eratosthenes(limit)}")  # print the list of primes
    sieve_of_eratosthenes(limit)  # print to console, or write to file
