# Matt Parker Maths Puzzles 19

from prettytable import PrettyTable


# Find the sums of primes squared which are divisible by the number of primes in that sum
def mpmp19(primes):
    table = PrettyTable()
    table.field_names = ["index", "prime", "sum of squares", "quotient"]
    sum_sq = 0
    index = 0
    for p in primes:
        index += 1
        sum_sq += p * p
        if sum_sq % index == 0:
            table.add_row([index, p, sum_sq, sum_sq / index])
    table.align = "r"
    print(table)
