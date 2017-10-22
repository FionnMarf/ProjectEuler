import time

def divisors():
    palindrome = 1
    for i in range(100, 1001):
        for j in range(i,1001):
            if j*i == reverse(j*i):
                if j*i > palindrome:
                    palindrome = j*i
    #palindromes.sort()
    print palindrome

def reverse(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r

if __name__ == "__main__":
    start_time = time.time()
    divisors()
    print "--- %s seconds ---" % (time.time() - start_time)
