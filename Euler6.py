import time


#foo(100)

def foo(n):
    printme = sumsquare(n) - squaresum(n)
    print printme

def squaresum(n):
    return ((n*(n+1)*(2*n+1))/6)

def sumsquare(n):
    return ((n*(n+1)/2)*(n*(n+1)/2))

if __name__ == '__main__':
    start_time = time.time()
    foo(100)
    print "--- %s seconds ---" % (time.time() - start_time)
#foo(100)
