from Algorithms import Checker
import os
import time


# Print files' name in 'Inputs' folder to help users.
def printDir(path):
    fileList = os.listdir(path)
    print(">> List of input files:")

    for name in fileList:
        print("  >> " + name)


# Print chessboard to screen
def printChessBoard(chessBoard):

    # Can not print if chess board is empty
    if not chessBoard:
        print("ChessBoard is empty! You have to create it first.")
        return

    size = len(chessBoard)  # size = 8
    for row in range(size):
        for col in range(size):

            # no newline if final column has not reached
            if col < size-1:
                # print white
                if chessBoard[row][col][1] == "WHITE":
                    if chessBoard[row][col][0] == "QUEEN":
                        print('Q' + " ", end='')
                    elif chessBoard[row][col][0] == "ROOK":
                        print('R' + " ", end='')
                    elif chessBoard[row][col][0] == "KNIGHT":
                        print('K' + " ", end='')
                    elif chessBoard[row][col][0] == "BISHOP":
                        print('B' + " ", end='')
                    else:
                        print('.' + " ", end='')
                # print black
                else:
                    if chessBoard[row][col][0] == "QUEEN":
                        print('q' + " ", end='')
                    elif chessBoard[row][col][0] == "ROOK":
                        print('r' + " ", end='')
                    elif chessBoard[row][col][0] == "KNIGHT":
                        print('k' + " ", end='')
                    elif chessBoard[row][col][0] == "BISHOP":
                        print('b' + " ", end='')
                    else:
                        print('.' + " ", end='')

            # newline in print because final column is reached
            else:
                # print white
                if chessBoard[row][col][1] == "WHITE":
                    if chessBoard[row][col][0] == "QUEEN":
                        print('Q' + "\n")
                    elif chessBoard[row][col][0] == "ROOK":
                        print('R' + "\n",)
                    elif chessBoard[row][col][0] == "KNIGHT":
                        print('K' + "\n",)
                    elif chessBoard[row][col][0] == "BISHOP":
                        print('B' + "\n",)
                    else:
                        print('.' + "\n",)
                # print black
                else:
                    if chessBoard[row][col][0] == "QUEEN":
                        print('q' + "\n",)
                    elif chessBoard[row][col][0] == "ROOK":
                        print('r' + "\n",)
                    elif chessBoard[row][col][0] == "KNIGHT":
                        print('k' + "\n")
                    elif chessBoard[row][col][0] == "BISHOP":
                        print('b' + "\n")
                    else:
                        print('.' + "\n")

    printConflictAmount(chessBoard)


# Print amount of detected conflict to screen
def printConflictAmount(chessBoard):
    totalA, totalB, queenA, rookA, bishopA, knightA, queenB, rookB, bishopB, knightB =\
        Checker.conflictChecker(chessBoard)
    # totalA, queenA, rookA, bishopA, knightA = Checker.conflictChecker(chessBoard)
    # totalB, queenB, rookB, bishopB, knightB = Checker.conflictCheckerB(chessBoard)

    print(str(totalA) + " ", end='')
    print(str(totalB))

    # ------------------ FOR DEBUGGING -----------------
    # print("Total conflict A : " + str(totalA))
    # print("Description:")
    # print("  Queen  : " + str(queenA))
    # print("  Rook   : " + str(rookA))
    # print("  Bishop : " + str(bishopA))
    # print("  Knight : " + str(knightA))
    # print("\n")
    # print("Total conflict B : " + str(totalB))
    # print("Description:")
    # print("  Queen  : " + str(queenB))
    # print("  Rook   : " + str(rookB))
    # print("  Bishop : " + str(bishopB))
    # print("  Knight : " + str(knightB))


# Output solution as file.
# Result is saved in 'Solutions' folder.
def printSolutionToFile(chessBoard, solType):
    # Use now's date and time as filename
    timestr = time.strftime("%Y%m%d-%H%M%S")

    # Create and write file
    outfile = open("Solutions/" + timestr + "-" + solType + ".txt", "w")

    # Check amount of conflict from chess board final state
    totalA, totalB, queenA, rookA, bishopA, knightA, queenB, rookB, bishopB, knightB =\
        Checker.conflictChecker(chessBoard)
    size = len(chessBoard)

    # write to file
    # Remember that chessboard elements is tuple.
    # Tuple structure : (<TYPE>, <COLOR>)
    for row in range(size):
        for col in range(size):

            # no newline if final column has not reached
            if col < size-1:
                # outfile.write white
                if chessBoard[row][col][1] == "WHITE":
                    if chessBoard[row][col][0] == "QUEEN":
                        outfile.write('Q' + " ")
                    elif chessBoard[row][col][0] == "ROOK":
                        outfile.write('R' + " ")
                    elif chessBoard[row][col][0] == "KNIGHT":
                        outfile.write('K' + " ")
                    elif chessBoard[row][col][0] == "BISHOP":
                        outfile.write('B' + " ")
                    else:
                        outfile.write('.' + " ")
                # outfile.write black
                else:
                    if chessBoard[row][col][0] == "QUEEN":
                        outfile.write('q' + " ")
                    elif chessBoard[row][col][0] == "ROOK":
                        outfile.write('r' + " ")
                    elif chessBoard[row][col][0] == "KNIGHT":
                        outfile.write('k' + " ")
                    elif chessBoard[row][col][0] == "BISHOP":
                        outfile.write('b' + " ")
                    else:
                        outfile.write('.' + " ")

            # newline in outfile.write because final column is reached
            else:
                # outfile.write white
                if chessBoard[row][col][1] == "WHITE":
                    if chessBoard[row][col][0] == "QUEEN":
                        outfile.write('Q' + "\n")
                    elif chessBoard[row][col][0] == "ROOK":
                        outfile.write('R' + "\n",)
                    elif chessBoard[row][col][0] == "KNIGHT":
                        outfile.write('K' + "\n",)
                    elif chessBoard[row][col][0] == "BISHOP":
                        outfile.write('B' + "\n",)
                    else:
                        outfile.write('.' + "\n",)
                # outfile.write black
                else:
                    if chessBoard[row][col][0] == "QUEEN":
                        outfile.write('q' + "\n",)
                    elif chessBoard[row][col][0] == "ROOK":
                        outfile.write('r' + "\n",)
                    elif chessBoard[row][col][0] == "KNIGHT":
                        outfile.write('k' + "\n")
                    elif chessBoard[row][col][0] == "BISHOP":
                        outfile.write('b' + "\n")
                    else:
                        outfile.write('.' + "\n")

    outfile.write("Total conflict A: " + str(totalA) + "\n")
    outfile.write("Total conflict B: " + str(totalB))
