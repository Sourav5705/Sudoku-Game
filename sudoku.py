n = 9
board = []
for i in range(n):
    l = [int(x) for x in input().split(" ")]
    board.append(l)
# board[0][0] = 2


def subgrid(board, row, col, x):
    rowl = rowu = coll = colu = 0
    if row >= 0 and row <= 2:
        rowl = 0
        rowu = 2
    elif row >= 3 and row <= 5:
        rowl = 3
        rowu = 5
    else:
        rowl = 6
        rowu = 8
    if col >= 0 and col <= 2:
        coll = 0
        colu = 2
    elif col >= 3 and col <= 5:
        coll = 3
        coll = 5
    else:
        coll = 6
        colu = 8
    for r in range(rowl, rowu+1):
        for c in range(coll, colu+1):
            if r == row and c == col:
                continue
            if board[r][c] == x:
                return True
    return False


def issafe(board, row, col, x):
    for j in range(n):
        if j == col:
            continue
        if board[row][j] == x:
            return False
    for j in range(n):
        if j == row:
            continue
        if board[j][col] == x:
            return False
    if subgrid(board, row, col, x):
        return False
    return True


def sudoku(board, row, col):
    if col >= n:
        row = row+1
        col = 0
    if row >= n or col >= n:
        return True
    if board[row][col] > 0:
        return sudoku(board, row, col+1)
    for i in range(1, 10):
        if issafe(board, row, col, i):
            board[row][col] = i
            if sudoku(board, row, col+1) == True:
                return True
            board[row][col] = 0
    return False


sudoku(board, 0, 0)
for i in range(n):
    for j in range(n):
        print(board[i][j], end=" ")
    print()
