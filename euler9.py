import math as math

def maketriples(n):
    i = 1.0
    j = 1.0
    while i < 1000:
        j = i+1.0
        while j < 1000:
            holder = math.sqrt(((i**2.0) + (j**2.0)))
            if holder == int(holder):
                print holder
                if (i + j + holder) == n:
                    returnme = [i, j, holder]
                    print "Success"
                    print returnme
                    return i*j*holder
            j += 1
        i += 1

if __name__ == '__main__':
    print maketriples(1000)
