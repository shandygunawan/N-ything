from random import randint
from IO import Parser


def createChessboard():
    # create a chessboard
    chessBoard = []
    size = 8
    for i in range(size):
        col = []
        for j in range(size):
            col.append(('.', "."))
        chessBoard.append(col)

    # read File's content
    chessPieces = Parser.readPiecesFile("Inputs/" + input(">> Enter filename: "))

    # randomize chess pieces' positions
    randomizer(chessBoard, chessPieces)

    print(">> Chess board created.")
    return chessBoard


def readChessboard():
    # read file's content
    return Parser.readChessBoardFile("Inputs/" + input(">> Enter filename: "))


# clear board from chess pieces
def clearBoard(chessBoard):
    size = len(chessBoard)
    for i in range(size):
        for j in range(size):
            chessBoard[i][j] = ('.', ".")


# Fill board boxes with chess pieces
def fillBoard(chessBoard, row, col, pieceType, color):
    if color == "WHITE":
        if pieceType == "KNIGHT":
            chessBoard[row][col] = ("KNIGHT", "WHITE")
        elif pieceType == "BISHOP":
            chessBoard[row][col] = ("BISHOP", "WHITE")
        elif pieceType == "ROOK":
            chessBoard[row][col] = ("ROOK", "WHITE")
        elif pieceType == "QUEEN":
            chessBoard[row][col] = ("QUEEN", "WHITE")
    elif color == "BLACK":
        if pieceType == "KNIGHT":
            chessBoard[row][col] = ("KNIGHT", "BLACK")
        elif pieceType == "BISHOP":
            chessBoard[row][col] = ("BISHOP", "BLACK")
        elif pieceType == "ROOK":
            chessBoard[row][col] = ("ROOK", "BLACK")
        elif pieceType == "QUEEN":
            chessBoard[row][col] = ("QUEEN", "BLACK")


# Create list of pieces from chess board for randomizer
def createPiecesList(chessBoard):
    size = len(chessBoard)
    piecesList = []
    for row in range(size):
        for col in range(size):
            if chessBoard[row][col] != ('.', "."):
                piecesList.append(chessBoard[row][col])

    return piecesList


# Create list of pieces from chess board with positions of each
def createPiecesListWithPos(chessBoard):
    size = len(chessBoard)
    piecesWithLoc = []
    for row in range(size):
        for col in range(size):
            if chessBoard[row][col] != ('.', "."):
                piecesWithLoc.append([chessBoard[row][col][0], chessBoard[row][col][1], col, row])
    return piecesWithLoc


# Randomizes chess pieces' position
def randomizer(chessBoard, chessList):
    clearBoard(chessBoard)
    size = len(chessBoard)-1
    for piece in chessList:
        while True:
            row = randint(0, size)
            col = randint(0, size)

            if chessBoard[row][col] == ('.', "."):
                break

        fillBoard(chessBoard, row, col, piece[0], piece[1])


# Random chess piece and return all position of the piece 
# Use for genetic algorithm
def random_genetic(chessBoard, chessList):
    size = 8
    for i in range(size):
        col = []
        for j in range(size):
            col.append(('.', "."))
        chessBoard.append(col)

    positionList = []
    for piece in chessList:
        while True:
            row = randint(0, 7)
            col = randint(0, 7)

            if chessBoard[row][col] == ('.', "."):
                break

        positionList.append([[row, col], piece[0], piece[1]])
        fillBoard(chessBoard, row, col, piece[0], piece[1])

    return positionList


def updateBoard(chessBoard, chessList):
    clearBoard(chessBoard)
    for piece in chessList:
        fillBoard(chessBoard, piece[0][0], piece[0][1], piece[1], piece[2])


def findPossibleMoves(chessPiece, chessBoard):
    # Finding all possible moves of a piece on the chessboard
    # chessPiece must contain [('PIECE TYPE') , ('PIECE COLOUR'), pieceColumnNumber, pieceRowNumber]
    # Use createPieceListWithPos
    possMoves = []

    if chessPiece[0] == "KNIGHT":
        possMoves.extend(knightMoves(chessPiece, chessBoard))
    elif chessPiece[0] == 'BISHOP':
        possMoves.extend(diagonalMoves(chessPiece, chessBoard))
    elif chessPiece[0] == 'ROOK':
        possMoves.extend(horizontalMoves(chessPiece, chessBoard))
        possMoves.extend(verticalMoves(chessPiece, chessBoard))
    elif chessPiece[0] == 'QUEEN':
        possMoves.extend(horizontalMoves(chessPiece, chessBoard))
        possMoves.extend(verticalMoves(chessPiece, chessBoard))
        possMoves.extend(diagonalMoves(chessPiece, chessBoard))
    return possMoves


# Finding possible horizontal moves
def horizontalMoves(chessPiece, chessBoard):
    hMoves = []
    rightBound = False
    leftBound = False
    # Finding moves for left hand side
    x = chessPiece[2] - 1
    y = chessPiece[3]
    while not leftBound and x >= 0:
        if chessBoard[y][x][0] == '.':
            hMoves.append([x, y])
            x -= 1
        else:
            leftBound = True
    # Finding moves for right hand side
    x = chessPiece[2] + 1
    while not rightBound and x <= 7:
        if chessBoard[y][x][0] == '.':
            hMoves.append([x, y])
            x += 1
        else:
            rightBound = True
    return hMoves


# Finding possible diagonal moves
def diagonalMoves(chessPiece, chessBoard):
    dMoves = []
    northWestBound = False
    northEastBound = False
    southWestBound = False
    southEastBound = False

    # Finding moves to the northWest
    x = chessPiece[2] - 1
    y = chessPiece[3] - 1
    while not northWestBound and x >= 0 and y >= 0:
        if chessBoard[y][x][0] == '.':
            dMoves.append([x, y])
            x -= 1
            y -= 1
        else:
            northWestBound = True

    # Finding moves to the northEast
    x = chessPiece[2] + 1
    y = chessPiece[3] - 1
    while not northEastBound and x <= 7 and y >= 0:
        if chessBoard[y][x][0] == '.':
            dMoves.append([x, y])
            x += 1
            y -= 1
        else:
            northEastBound = True
    
    # Finding moves to the southWest
    x = chessPiece[2] - 1
    y = chessPiece[3] + 1
    while not southWestBound and x >= 0 and y <= 7:
        if chessBoard[y][x][0] == '.':
            dMoves.append([x, y])
            x -= 1
            y += 1
        else:
            southWestBound = True
    
    # Finding moves to the southEast
    x = chessPiece[2] + 1
    y = chessPiece[3] + 1
    while not southEastBound and x <= 7 and y <= 7:
        if chessBoard[y][x][0] == '.':
            dMoves.append([x, y])
            x += 1
            y += 1
        else:
            southEastBound = True

    return dMoves


# Finding possible vertical moves
def verticalMoves(chessPiece, chessBoard):
    vMoves = []
    upBound = False
    downBound = False

    # Finding moves up
    x = chessPiece[2]
    y = chessPiece[3] - 1
    while not upBound and y >= 0:
        if chessBoard[y][x][0] == '.':
            vMoves.append([x, y])
            y -= 1
        else:
            upBound = True

    # Finding moves down
    y = chessPiece[3] + 1
    while not downBound and y <= 7:
        if chessBoard[y][x][0] == '.':
            vMoves.append([x, y])
            y += 1
        else:
            downBound = True
    return vMoves


# Finding possible knight moves
def knightMoves(chessPiece, chessBoard):
    kMoves = []
    
    # Finding moves of a knight 
    x = chessPiece[2]
    y = chessPiece[3]

    if x - 2 >= 0 and y - 1 >= 0 and chessBoard[y-1][x-2][0] == '.':
        kMoves.append([x-2, y-1])
    if x - 2 >= 0 and y + 1 <= 7 and chessBoard[y+1][x-2][0] == '.':
        kMoves.append([x-2, y+1])
    if x + 2 <= 7 and y - 1 >= 0 and chessBoard[y-1][x+2][0] == '.':
        kMoves.append([x+2, y-1])
    if x + 2 <= 7 and y + 1 <= 7 and chessBoard[y+1][x+2][0] == '.':
        kMoves.append([x+2, y+1])
    if x - 1 >= 0 and y - 2 >= 0 and chessBoard[y-2][x-1][0] == '.':
        kMoves.append([x-1, y-2])
    if x - 1 >= 0 and y + 2 <= 7 and chessBoard[y+2][x-1][0] == '.':
        kMoves.append([x-1, y+2])
    if x + 1 <= 7 and y - 2 >= 0 and chessBoard[y-2][x+1][0] == '.':
        kMoves.append([x+1, y-2])
    if x + 1 <= 7 and y + 2 <= 7 and chessBoard[y+2][x+1][0] == '.':
        kMoves.append([x+1, y+2])
        
    return kMoves
