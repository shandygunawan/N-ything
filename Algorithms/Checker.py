# check if a position is inside the board
def checkBoundary(i,j):
    return i >= 0 and j >= 0 and i < 8 and j < 8


# Check box
def checkBox(chessBoard, row, col):
    if chessBoard[row][col] != ('.', ".") :
        return True
    else:
        return False


# Check horizontal conflict
def checkHorizontalConflict(chessBoard, row, col, color):
    countSame = 0
    countDiff = 0
    # Check left
    for j in range(col-1, -1, -1):
        if checkBox(chessBoard, row, j):
            if (color == chessBoard[row][j][1]) :
                countSame += 1
                break
            else :
                countDiff += 1
                break

    # Check right
    for j in range(col+1, len(chessBoard)):
        if checkBox(chessBoard, row, j):
            if (color == chessBoard[row][j][1]) :
                countSame += 1
                break
            else :
                countDiff += 1
                break

    return countSame, countDiff


# check vertical conflict
def checkVerticalConflict(chessBoard, row, col, color):
    countSame = 0
    countDiff = 0
    # check up
    for i in range(row-1, -1, -1):
        if checkBox(chessBoard, i, col):
            if (color == chessBoard[i][col][1]) :
                countSame += 1
                break
            else :
                countDiff += 1
                break

    # check down
    for i in range(row+1, len(chessBoard)):
        if checkBox(chessBoard, i, col):
            if (color == chessBoard[i][col][1]) :
                countSame += 1
                break
            else :
                countDiff += 1
                break

    return countSame, countDiff


# check both diagonal conflict
def checkDiagonalConflict(chessBoard, row, col, color):
    # a piece at (p, q) is on the same diagonal as a piece at (r, s) if abs(p - r) == abs (q - s)
    size = len(chessBoard)
    countSame = 0
    countDiff = 0
    # check up left
    i = row-1
    for j in range(col-1, -1, -1):
        if checkBoundary(i, j) and checkBox(chessBoard, i, j):
            if (color == chessBoard[i][j][1]) :
                countSame += 1
                break
            else :
                countDiff += 1
                break
        else:
            i -= 1

    # check Up right
    i = row-1
    for j in range(col+1, size):
        if checkBoundary(i, j) and checkBox(chessBoard, i, j):
            if (color == chessBoard[i][j][1]) :
                countSame += 1
                break
            else :
                countDiff += 1
                break
        else:
            i -= 1

    # check down left
    i = row+1
    for j in range(col-1, -1, -1):
        if checkBoundary(i, j) and checkBox(chessBoard, i, j):
            if (color == chessBoard[i][j][1]) :
                countSame += 1
                break
            else :
                countDiff += 1
                break
        else:
            i += 1

    # check down right
    i = row+1
    for j in range(col+1, size):
        if checkBoundary(i, j) and checkBox(chessBoard, i, j):
            if (color == chessBoard[i][j][1]) :
                countSame += 1
                break
            else :
                countDiff += 1
                break
        else:
            i += 1

    # check up
    # counter = 0
    # for i in range(row-1, -1, -1):
    #     if counter == 2:
    #         break
    #
    #     for j in range(size):
    #         if counter == 2:
    #             break
    #
    #         if abs(row - i) == abs(col - j) and chessBoard[i][j] != ('.', "."):
    #             if chessBoard[i][j][1] == color:
    #                 return True
    #             else:
    #                 counter += 1
    #
    # # check down
    # counter = 0
    # for i in range(row+1, size):
    #     if counter == 2:
    #         break
    #
    #     for j in range(size):
    #         if counter == 2:
    #             break
    #
    #         if abs(row - i) == abs(col - j) and chessBoard[i][j] != ('.', "."):
    #             if chessBoard[i][j][1] == color:
    #                 return True
    #             else:
    #                 counter += 1

    return countSame, countDiff


# check conflict for knight (L range)
def checkKnightConflict(chessBoard, row, col, color):
    deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]

    countSame = countDiff = 0

    for (i, j) in deltas:
        x = col + j
        y = row + i

        if checkBoundary(y, x):
            if checkBox(chessBoard, y, x):
                if (color == chessBoard[y][x][1]) :
                    countSame += 1
                    break
                else :
                    countDiff += 1
                    break

    return countSame, countDiff


# Conflict A checker (same color)
def conflictChecker(chessBoard):
    size = len(chessBoard)
    countSame = countDiff = 0
    rookSameConflict = rookDiffConflict = 0
    queenSameConflict = queenDiffConflict = 0
    bishopSameConflict = bishopDiffConflict = 0
    knightSameConflict = knightDiffConflict = 0
    totalSameConflict = totalDiffConflict = 0

    for row in range(size):
        for col in range(size):
            if chessBoard[row][col][0] == ("ROOK"):  # ROOK
                countSame, countDiff = rookConflictChecker(chessBoard, row, col)
                rookSameConflict += countSame
                rookDiffConflict += countDiff

            elif chessBoard[row][col][0] == ("BISHOP"):  # BISHOP
                countSame, countDiff = bishopConflictChecker(chessBoard, row, col)
                bishopSameConflict += countSame
                bishopDiffConflict += countDiff

            elif chessBoard[row][col][0] == ("QUEEN"):  # QUEEN
                countSame, countDiff = queenConflictChecker(chessBoard, row, col)
                queenSameConflict += countSame
                queenDiffConflict += countDiff

            elif chessBoard[row][col][0] == ("KNIGHT"):  # KNIGHT
                countSame, countDiff = knightConflictChecker(chessBoard, row, col)
                knightSameConflict += countSame
                knightDiffConflict += countDiff

    totalSameConflict = rookSameConflict + knightSameConflict + queenSameConflict + bishopSameConflict
    totalDiffConflict = rookDiffConflict + knightDiffConflict + queenDiffConflict + bishopDiffConflict

    return totalSameConflict, totalDiffConflict, queenSameConflict, rookSameConflict, bishopSameConflict, knightSameConflict, +\
            queenDiffConflict, rookDiffConflict , bishopDiffConflict , knightDiffConflict

def rookConflictChecker(chessBoard, row, col) :
    countSame = sameConflict = 0
    countDiff = diffConflict = 0
    if chessBoard[row][col][1] == "WHITE" :
        sameConflict, diffConflict = checkHorizontalConflict(chessBoard, row, col, "WHITE")
        countSame += sameConflict
        countDiff += diffConflict
        sameConflict, diffConflict = checkVerticalConflict(chessBoard, row, col, "WHITE")
        countSame += sameConflict
        countDiff += diffConflict
    else : 
        sameConflict, diffConflict = checkHorizontalConflict(chessBoard, row, col, "BLACK")
        countSame += sameConflict
        countDiff += diffConflict
        sameConflict, diffConflict = checkVerticalConflict(chessBoard, row, col, "BLACK")
        countSame += sameConflict
        countDiff += diffConflict

    return countSame, countDiff

def bishopConflictChecker(chessBoard, row, col) :
    countSame = sameConflict = 0
    countDiff = diffConflict = 0
    if chessBoard[row][col][1] == "WHITE" :
        sameConflict, diffConflict = checkDiagonalConflict(chessBoard, row, col, "WHITE")
        countSame += sameConflict
        countDiff += diffConflict
    else : 
        sameConflict, diffConflict = checkDiagonalConflict(chessBoard, row, col, "BLACK")
        countSame += sameConflict
        countDiff += diffConflict
    
    return countSame, countDiff


def queenConflictChecker(chessBoard, row, col) :
    countSame = sameConflict = 0
    countDiff = diffConflict = 0
    if chessBoard[row][col][1] == "WHITE" :
        sameConflict, diffConflict = checkHorizontalConflict(chessBoard, row, col, "WHITE")
        countSame += sameConflict
        countDiff += diffConflict
        sameConflict, diffConflict = checkVerticalConflict(chessBoard, row, col, "WHITE")
        countSame += sameConflict
        countDiff += diffConflict
        sameConflict, diffConflict = checkDiagonalConflict(chessBoard, row, col, "WHITE")
        countSame += sameConflict
        countDiff += diffConflict
    else : 
        sameConflict, diffConflict = checkHorizontalConflict(chessBoard, row, col, "BLACK")
        countSame += sameConflict
        countDiff += diffConflict
        sameConflict, diffConflict = checkVerticalConflict(chessBoard, row, col, "BLACK")
        countSame += sameConflict
        countDiff += diffConflict
        sameConflict, diffConflict = checkDiagonalConflict(chessBoard, row, col, "BLACK")
        countSame += sameConflict
        countDiff += diffConflict

    return countSame, countDiff


def knightConflictChecker(chessBoard, row, col) :
    countSame = sameConflict = 0
    countDiff = diffConflict = 0
    if chessBoard[row][col][1] == "WHITE" :
        sameConflict, diffConflict = checkKnightConflict(chessBoard, row, col, "WHITE")
        countSame += sameConflict
        countDiff += diffConflict
    else : 
        sameConflict, diffConflict = checkKnightConflict(chessBoard, row, col, "BLACK")
        countSame += sameConflict
        countDiff += diffConflict

    return countSame, countDiff

       
def conflictCheckerB(chessBoard):
    size = len(chessBoard)
    totalConflict = queenConflict = rookConflict = bishopConflict = knightConflict = 0
