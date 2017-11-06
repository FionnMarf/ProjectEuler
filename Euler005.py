def main():
    p = 2*3*5*7*11*13*17*19
    finished = False
    increment = 1
    while not finished:
        finished = True
        for i in range(1, 20):
            if p%i != 0:
                finished = False
        if finished == True:
            print p
        increment += 1
        p *= increment

if __name__ == '__main__':
    main()
