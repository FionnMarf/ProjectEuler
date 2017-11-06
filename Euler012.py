
"""
Problem 12: Find the first triangular number with more than 500 divisors
https://projecteuler.net/problem=12

This is a little bit tricky and this number is probably going to be pretty
big, so first lets find the smallest number with 500 divisors

So, we first need the prime factors of 500 which are 5^3 and 2^2
We now expect our number with 500 divisors to be the smallest number written as
p1^a * p2^b * p3^c ... Pn^i with the indicies equal to the prime factors of 500
+1
So we expect powers 4, 4, 4, 1, 1
Some observation finds 2^4 * 3^4 * 5*4 * 7 * 11
or 62370000

n^2 + n - 2c = 0

Now, triangular numbers are of the form (n*(n+1))/2 so this says 2 must be a factor
the next triangle number after our lower bound can be found with a quadratic
T(11168) or 62367696

Note that this is a heuristic argument and not a proven correct solution, as I have
not proven that the first triangle number with 500+ divisors is larger than T11168
It is just usually true that this is the case to reduce the number of computations

In this instance it works, in an instance where I have no means of checking
my solution is correct I would have to either prove my above estimate
rigorously, or begin from n = 1
"""

import math
import time

def triangles():
    n = 11168
    finished = False
    while not finished:
        triangle = (n*(n+1))/2
        if factors(triangle) > 500:
            return triangle
        n += 1

def factors(n):
    returnme = 0
    i = 1
    stop = math.floor(math.sqrt(n))
    if stop == math.sqrt(n):
        returnme += 1
    while i < stop:
        if n%i == 0:
            returnme += 2
        i += 1
    return returnme




if __name__ == '__main__':
    start_time = time.time()
    print triangles()
    print "--- %s seconds ---" % (time.time() - start_time)
