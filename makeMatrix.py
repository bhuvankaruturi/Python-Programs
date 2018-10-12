#create a matrix of specified 'size', elements 'start' value and should the elements be incremented
def makeMatrix(size, start, doIncrement):
    a = []
	
    num = start
    try:
        if size <= 0:
           raise Exception("The size cannot be negative or zero")
        else:
            for x in range(size):
                a.append([])

            for x in range(size):
                for y in range(size):
                    a[x].append(num)
                    if doIncrement:
                        num += 1
            return a
    except Exception as error:
        print(error)

#method to print the matrix passed as argument
def printMatrix(matrix):
    a = matrix
    if(a != None):
        for x in range(len(a)):
            for y in range(len(a[x])):
                print(a[x][y], end='\t')
            print()
    else:
        print("The matrix is null or size is zero")

#Method to add numbers in a sequence to upper L
def upperL(mat, row, col, start):
    a = mat
    num = start
    endRow = len(a) - row
    endCol = len(a) - col
    if endRow - 1 == row and endCol - 1 == col:
        a[row][col] = num + 1
        return a
    for x in range(row, endRow):
        for y in range(col, endCol):
            num += 1
            if x == row:
                a[x][y] = num
            else:
                a[x][endCol - 1] = num
                break
    #print()
    #printMatrix(a)
    return lowerL(a, endRow - 1, endCol - 2, num)


#Method to add numbers in a sequence to lower L
def lowerL(mat, row, col, start):
    a = mat
    endRow = len(a) - 1 - col
    endCol = len(a) - 1 - row
    num = start
    if endRow == row and endCol == col:
        a[row][col] = num + 1
        return a
    else:
        for x in range(row, endRow - 1, -1):
            for y in range(col, endCol - 1, -1):
                num += 1
                if x == row:
                    a[x][y] = num
                else:
                    a[x][endCol] = num
                    break
        #print()
        #printMatrix(a)
        return upperL(a, endRow, endCol + 1, num)

#creation of matrix with index 2, starting element 0, setting element values to be incremented as False
mat = makeMatrix(2, 0, False)
printMatrix(mat)

#modify the created matrix to add numbers in a circular pattern.
def modifyMatrix(mat):
    if (mat != None):
        mat = upperL(mat, 0, 0, 0)
        print()
        printMatrix(mat)

modifyMatrix(mat)