def readPiecesFile(filename):
    print(">> Reading file...\n")
    # Read per line & store to list
    with open(filename) as infile:
        content = infile.readlines()
    infile.close()

    # strip newline
    chessPieces = [x.strip() for x in content]

    # transform contents to tuples
    piecesList = []
    for piece in chessPieces:
        pieceData = piece.split(" ")
        # pieceData[0] = Color {WHITE, BLACK}
        # pieceData[1] = Type {KNIGHT, BISHOP, ROOK, QUEEN}
        # pieceData[2] = Amount {1, 2, 3, ..., 64}

        tempTuple = (pieceData[1], pieceData[0])

        for i in range(int(pieceData[2])):
            piecesList.append(tempTuple)

    return piecesList


def readChessBoardFile(filename):
    print(">> Reading file...\n")

    # Create a chessboard
    chessBoard = []

    # Read per line & store to list
    with open(filename) as infile:
        content = infile.readlines()
    infile.close()

    # strip newline
    content = [x.strip() for x in content]

    for chessRow in content:
        chessRowList = chessRow.split(" ")
        toAppend = []

        for box in chessRowList:
            if box == '.':
                toAppend.append(('.', "."))
            elif box == 'Q':
                toAppend.append(("QUEEN", "WHITE"))
            elif box == 'R':
                toAppend.append(("ROOK", "WHITE"))
            elif box == 'K':
                toAppend.append(("KNIGHT", "WHITE"))
            elif box == 'B':
                toAppend.append(("BISHOP", "WHITE"))
            elif box == 'q':
                toAppend.append(("QUEEN", "BLACK"))
            elif box == 'r':
                toAppend.append(("ROOK", "BLACK"))
            elif box == 'k':
                toAppend.append(("KNIGHT", "BLACK"))
            elif box == 'b':
                toAppend.append(("BISHOP", "BLACK"))

        chessBoard.append(toAppend)

    return chessBoard
