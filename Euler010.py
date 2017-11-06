import math as math

def sumlist(primelist):
    i = 0
    holder = 0
    while i < len(primelist):
        holder += primelist[i]
        i += 1
    return holder

def checkprime(p): #Be sure and begin at p >= 5
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
    primelist = [2, 3]
    i = 5 #My primechecking algo only works if you begin at 5 or higher
    while i < n:
        if checkprime(i):
            primelist.append(i)
        i += 1
    print sumlist(primelist)

if __name__ == '__main__':
    main(2000000)
