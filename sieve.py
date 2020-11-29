def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries in it as True.
    # After the sieve a value in prime[i] will
    # only be True if it is a prime number.
    prime = [True for _ in range(n + 1)]

    # Use the sieve to filter out all multiples of primes as they are verified
    # The classic sieve normally uses p <= sqrt(n) as the limit,
    # but sqrt() is comparatively slower than multiplication
    # The first two numbers (0 and 1) are not prime, and are not used in the sieve or output
    p = 2
    while p * p <= n:

        # If prime[p] is True, then it is a prime
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

    # Write primes to file in current directory (one number per line)
    file = open("prime.txt", "wt")  # Open file for writing text (truncate to 0 length if it exists)
    file.write(f"Primes up to {n}\n")
    for p in range(2, n + 1):
        if prime[p]:
            file.write(f"{p}\n")
    file.close()

