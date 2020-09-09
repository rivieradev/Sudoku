from math import sqrt, floor

def isRowOk(table, row, value):
    for i in range(len(table)):
        if(table[row][i] == value):
            return False
    return True

def isColOk(table, col, value):
    for i in range(len(table)):
        if(table[i][col] == value):
            return False
    return True

def isBoxOk(table, row, col, value):
    boxSize = floor(sqrt(len(table)))
    boxRowStart = row - row % boxSize
    boxColStart = col - col % boxSize

    for i in range(boxRowStart, boxRowStart + boxSize):
        for j in range(boxColStart, boxColStart + boxSize):
            if(table[i][j] == value):
                return False
    return True

def areConstrainsOk(table, row, col, value):
    return isRowOk(table, row, value) and isColOk(table, col, value) \
        and isBoxOk(table, row, col, value)

def findEmptyLocation(table, loc):
    for i in range(len(table)):
        for j in range(len(table)):
            if(table[i][j] == 0):
                loc[0] = i
                loc[1] = j
                return True
    return False

def backtrackingSolution(table):
    loc = [0, 0]
    if (not findEmptyLocation(table, loc)):
        return True

    row = loc[0]
    col = loc[1]

    for value in range(1,10):
        if(areConstrainsOk(table, row, col, value)):
            table[row][col] = value
            if(backtrackingSolution(table)):
                return True
            table[row][col] = 0
    return False

def printSudoku(table): 
    for i in range(len(table)): 
        print(table[i]), print(" ") 

if __name__=="__main__": 
      
    # creating a 2D array for the grid 
    sudoku = [[0 for x in range(9)]for y in range(9)] 
      
    # assigning values to the grid 
    sudoku = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0]] 
      
    # if success print the puzzle 
    if(backtrackingSolution(sudoku)): 
        printSudoku(sudoku) 
    else: 
        print("No solution exists")