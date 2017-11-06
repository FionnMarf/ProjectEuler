def main(filename):
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            element = [int(x) for x in line.split(" ")]
            matrix.append(element)
    print productsearch(matrix)

def rowsearch(matrix):
    returnme = 1
    i = j = 0
    while i < 17:
        while j < 20:
            holder = (matrix[i][j]) * (matrix[i+1][j]) * (matrix[i+2][j]) * (matrix[i+3][j])
            if (holder > returnme):
                returnme = holder
            j += 1
        i += 1
    return returnme


def columnsearch(matrix):
    returnme = 1
    i = j = 0
    while i < 20:
        while j < 17:
            holder = (matrix[i][j]) * (matrix[i][j+1]) * (matrix[i][j+2]) * (matrix[i][j+3])
            if (holder > returnme):
                returnme = holder
            j += 1
        i += 1
    return returnme


def listcheck(matrix):
    returnme = 1
    i = 3
    while i < len(matrix)-4:
        j = 0
        while j < len(matrix[i])-3:
            holder = (matrix[i][j]) * (matrix[i][j+1]) * (matrix[i][j+2]) * (matrix[i][j+3])
            if (holder > returnme):
                returnme = holder
            j += 1
        i += 1
    return returnme


def diagonalsearch(matrix):
    fordiag = [[] for i in range(39)]
    backdiag = [[] for i in range(len(fordiag))]
    minbd = -19
    y = 0
    while y < 20:
        x = 0
        while x < 20:
            fordiag[x+y].append(matrix[y][x])
            backdiag[-minbd + x-y].append(matrix[y][x])
            x += 1
        y += 1
    return max(listcheck(backdiag), listcheck(fordiag))



def productsearch(matrix):
    rm = rowsearch(matrix)
    cm = columnsearch(matrix)
    dm = diagonalsearch(matrix)
    return max(rm, cm, dm)

if __name__ == '__main__':
    main('euler11.txt')
