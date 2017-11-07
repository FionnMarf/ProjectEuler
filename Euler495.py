"""Project Euler 495:
How many ways can you write 10000! as a product of 30 distinct integers
Give your answer %1 000 000 007

This is my first attempt at a maximum difficulty problem

10000! = Product of P1^a1, P2^a2 ... Pn^an
with P1, .. ,Pn the set of primes less than 10000
and a1, .. ,an the number of times each prime divides a number under 10000
any distinct seperation of these primes defines a way to write n as a product of
k distinct integers
leaving us with a simple(ish) combinatorics problem around how we choose our partition point

Why does this work?
The fundamental Theoreom of Arithmatic
All numbers can be factored into a unique product of prime numbers

Current Sub-Problem: Combinatorics
We have 29486 prime factors
so 29485 possible cutting points (1 is not included in the factor list)
29 cuts to be made
no 2 partitions can have both the same length and same elements
i.e. 2 partitions Q1 Q2 are equivalent if Q1 and Q2 are elementwise equivalent
So, we need the total number of cutting points less the number of cutting points
in which at least 2 of the partitions are equivalent


Footnote - Topics that have arisen in my solution so far:
Number Theory
Group Theory
Combinatorics
"""


import math
import time
import numpy as numpy

#Return a list of the exponenets (indicies) of each prime in primelist
def factorise(n, primelist):
    i = 1
    k = 0
    exponentlist = []

    while k < len(primelist):
        exponentlist.append(0)
        k += 1

    p = 0
    total = 0
    finished = False
    while p < len(primelist):
        if i <= math.floor((math.log(n)/math.log(primelist[p]))):
            addme = n/(primelist[p]**i)
            exponentlist[p] += addme
            total += addme
            i += 1
        else:
            i = 1
            finished = True
            p += 1
    print total
    return [exponentlist, total]


#Generates a list of all prime numbers up to some value n
#checkprime(p) only works for primes larger than or equal to 5 so we included
#2 and 3 by default
def listprimes(n):
    finished = False
    primelist = [2, 3]
    i = 5

    while not finished:
        i += 2
        if checkprime(i):
            primelist.append(i)
        if i > n:
            finished = True

    return primelist



def checkprime(p):
    if p%6 == 5 or p%6 == 1:
        stop = math.floor(math.sqrt(p))
        i = 5

        while i <= stop:
            if p%i == 0 or p%(i + 2) == 0:
                return False
            else:
                i += 6
        return True
    else:
        return False


"""
    This part is proving a little trickier than the rest and as far as I know
    will require a complex implementation of Polya's Enumeration Theorem
    (See this article on Wolfram http://mathworld.wolfram.com/PolyaEnumerationTheorem.html)
    And is currently a work in progress
"""
def partitions(parts, exponentlist, factors):
    print "test"


#These next 2 functions might not be immediately necessary but the phrasing of the question suggests they will be

#we need every number modulo 1 000 000 007,
#the numbers we are dealing with are too big otherwise
def modchoose(n, k):
    return (modfactorial(n)/(modfactorial(k)*(modfactorial(n-k))))

#A replacement to the factorial function that takes results modulo a
def modfactorial(n):
    a = 1000000007 #1 000 000 007 we are giving our answer modulo a
    returnme = 1
    while n > 1:
        returnme *= n
        returnme = (returnme%a)
        n -= 1
    return returnme


def main(n):
    primes = listprimes(n)
    holder = factorise(n, primes) #this returns a list containing both the exponents and the total number of factors
    exponentlist = holder[0]
    factors = holder[1]
    k = 30
    print partitions(k, exponentlist, factors)%1000000007
    #we are interested in 1 value, the number of ways to write n as the product of k distinct integers
    #combinations() should return that value



if __name__ == '__main__':
    start_time = time.time()
    main(10000)
    print "--- %s seconds ---" % (time.time() - start_time)
