# Matt Parker Maths Puzzles 19

# Find the sums of primes squared which are divisible by the number of primes in that sum


def mpmp19(primes):
    sum_sq = 0
    index = 0
    for p in primes:
        index += 1
        sum_sq += p * p
        if sum_sq % index == 0:
            print(f"{p} is prime number {index}.\nThe sum of squares of {index} primes = {sum_sq} and is divisible by {index}")

