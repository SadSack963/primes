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

    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            # print(f"{p}, ", end="")
            primes.append(p)
    return primes


# driver program
primes = []
if __name__ == '__main__':
    n = 100
    print(f"Following are the prime numbers smaller than or equal to {n} {sieve_of_eratosthenes(n)}")
