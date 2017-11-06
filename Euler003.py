import math as math

#Need a reasonably efficient (sub exponential?) factorization algorithm for the largest prime factor
#ideas
#begin at sqrt(n) and work backwards until a prime factor is found (still exponential)

def factorize(n):
    #finished = False
    new = math.floor(math.sqrt(n))
    print new
    i = 3
    primelist = []
    while (i <= new):
        if n%i == 0:
            if checkprime(i):
                primelist.append(i)
                print i
            i += 2
        elif i >= new:
            return primelist
        else:
            i += 2
        #print i

def checkprime(p): #composites made up of 2 and 3 are excluded
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

if __name__ == "__main__":
    #print factorize(600851475143)
    print factorize(3646740004375894379)
