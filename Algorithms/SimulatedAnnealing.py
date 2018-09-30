from Algorithms import BoardHandler, Checker, hc
from IO import Printer, Parser
from random import randint
import copy
import math


# Solve problem using Simulated Annealing algorithm
def simulatedAnnealing(maxTry, chessBoard) :
    # Initialization
    mTry = iterator = maxTry

    # Copying initiate board
    bestResult = copy.deepcopy(chessBoard)
    ts0, td0, qs0, qd0, rs0, rd0, bs0, bd0, ks0, kd0 = Checker.conflictChecker(bestResult)
    Value = ts0 - td0
    
    # Improved and accepted states counter
    improved = accepted = 0

    # Outer loop, which loops the 
    while iterator > 0:
        T = math.log(mTry - iterator + 1, math.exp(1))
        
        tempBoard = copy.deepcopy(bestResult)
        tempList = BoardHandler.createPiecesListWithPos(tempBoard)
        randPiece = tempList[randint(0, len(tempList)-1)]

        randRow = randint(0, 7)
        randCol = randint(0, 7)
        while tempBoard[randRow][randCol] != ('.', ".") :
            randRow = randint(0, 7) 
            randCol = randint(0, 7)
        tempBoard[randPiece[3]][randPiece[2]] = ('.', ".")
        tempBoard[randRow][randCol] = (randPiece[0], randPiece[1])

        ts1, td1, qs1, qd1, rs1, rd1, bs1, bd1, ks1, kd1 = Checker.conflictChecker(tempBoard)
        tempValue = ts1 - td1
        if tempValue <= Value :
            bestResult = copy.deepcopy(tempBoard)
            Value = tempValue
            improved += 1
        elif tempValue > Value :
            sigmoidFunc = math.floor(math.exp(-T)) * 100
            randomNum = randint(0,100)
            if sigmoidFunc > randomNum :
                bestResult = copy.deepcopy(tempBoard)
                Value = tempValue
                accepted += 1

        iterator -= 1
    print(improved)
    print(accepted)
    Printer.printSolutionToFile(bestResult, "SimulatedAnnealing")
    return bestResult

