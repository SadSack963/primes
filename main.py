# Sieve of Eratosthenes
# =====================

# My thanks to Geeks for Geeks for the original implementation of the sieve algorithm
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

# Python program to generate all primes <= a given number using the Sieve of Eratosthenes

from sieve import sieve_of_eratosthenes
from nineteen import mpmp19
import time

# Start
if __name__ == '__main__':
    print("Sieve of Eratosthenes\n"
          "=====================")
    limit = int(input("Find all primes up to : "))

    # print(f"List of primes: {sieve_of_eratosthenes(limit)}")  # print the list of primes
    # sieve_of_eratosthenes(limit)  # print to console, or write to file
    t0 = time.gmtime()
    primes = sieve_of_eratosthenes(limit)

    t1 = time.gmtime()
    mpmp19(primes)

    t2 = time.gmtime()
    print(f"It took {t1-t0} seconds to generate the primes below {limit}.")
    print(f"It took {t2-t1} seconds to find the MPMP19 solutions.")
    print(f"The entire process took {t2-t0} seconds.")