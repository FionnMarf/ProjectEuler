import math as math

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

def main(n):
    checkme = 5
    primelist = [2, 3]
    finished = False
    while not finished:
        if checkprime(checkme):
            primelist.append(checkme)
        if len(primelist) == n:
            print primelist[n-1]
            finished = True
        checkme += 2

if __name__ == '__main__':
    main(10001)
