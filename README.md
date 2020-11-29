<h1>Solution to Matt Parker's "The 19 Challenge"</h1>

https://www.youtube.com/watch?v=tBXGIXEV7tI&t=2s

This Python program generates primes up to a given limit, and then sums the squares of these primes.
If the sum is divisible by the number of primes, then this number is a solution to the puzzle.

Sample output:
<pre>
Sieve of Eratosthenes
=====================
Find all primes up to : 10000000
1606673711.4018526: Generating primes...
1606673713.958588: Checking for solutions...
+--------+---------+--------------------+-----------------+
|  index |   prime |     sum of squares |        quotient |
+--------+---------+--------------------+-----------------+
|      1 |       2 |                  4 |             4.0 |
|     19 |      67 |              24966 |          1314.0 |
|     37 |     157 |             263736 |          7128.0 |
|    455 |    3217 |         1401992410 |       3081302.0 |
|    509 |    3637 |         2040870112 |       4009568.0 |
|    575 |    4201 |         3054955450 |       5312966.0 |
|  20597 |  231947 |    346739122490032 |   16834447856.0 |
| 202717 | 2790569 | 499159078330000800 | 2462344442400.0 |
+--------+---------+--------------------+-----------------+
1606673711.4018526: Finished!

It took 2.5567352771759033 seconds to generate the primes below 10000000.
It took 0.13164854049682617 seconds to find the MPMP19 solutions.
The entire process took 2.6883838176727295 seconds.

Process finished with exit code 0
</pre>pre>