# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is NOT a prime, else true.
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:  # p <= sqrt(n) but sqrt() is comparatively slow!

        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # # Print all prime numbers to console
    # for p in range(2, n + 1):
    #     if prime[p]:
    #         print(f"{p}, ", end="")

    # # Create a list of primes (CSV)
    # primes = []
    # for p in range(2, n + 1):
    #     if prime[p]:
    #         primes.append(p)
    # return primes

    # Write primes to file (one number per line)
    file = open("prime.txt", "wt")  # Open file for writing text (truncate to 0 length if it exists)
    for p in range(2, n + 1):
        if prime[p]:
            file.write(f"{p}\n")
    file.close()


# Start
if __name__ == '__main__':
    n = int(input("Find all primes up to : "))

    # print(f"List of primes: {sieve_of_eratosthenes(n)}")
    sieve_of_eratosthenes(n)  # print to console, or write to file
