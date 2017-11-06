import math as math

def fibsequence(end):
    gr = 1.61803399
    final = math.floor((math.log((math.sqrt(5)*end) + 0.5)/math.log(gr)))
    returnme = 0
    i = 3
    while (i < final):
        returnme += fibindex(i)
        i += 3
    return returnme

def fibindex(n):
    gr = 1.61803399
    Fn = math.floor(((gr**n)/math.sqrt(5))+0.5)
    print Fn
    return Fn

if __name__ == "__main__":
    print fibsequence(8000000)

