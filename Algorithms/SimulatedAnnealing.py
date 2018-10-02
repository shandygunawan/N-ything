from Algorithms import BoardHandler, Checker, hc
from IO import Printer, Parser
from random import randint
import copy
import math

# Solve problem using Simulated Annealing algorithm

def simulatedAnnealing(maxTry, chessBoard) :
    # Initialization
    mTry = iterator = maxTry

    # Copy initiate board and count the value
    bestResult = copy.deepcopy(chessBoard)
    ts0, td0, qs0, qd0, rs0, rd0, bs0, bd0, ks0, kd0 = Checker.conflictChecker(bestResult)
    Value = ts0 - td0
    
    # Improved and accepted states counter
    improved = accepted = 0

    # Outer loop, which randomizes state until a number of steps
    while iterator > 0 :
        # Function that set the temperature
        T = math.log(mTry - iterator + 1, math.exp(1))
        
        # Generate a random state
        tempBoard = copy.deepcopy(bestResult)
        tempList = BoardHandler.createPiecesListWithPos(tempBoard)
        randPiece = tempList[randint(0, len(tempList)-1)]

        # Randomizes a piece's position
        randRow = randint(0, 7)
        randCol = randint(0, 7)
        while tempBoard[randRow][randCol] != ('.', ".") :
            randRow = randint(0, 7) 
            randCol = randint(0, 7)
        tempBoard[randPiece[3]][randPiece[2]] = ('.', ".")
        tempBoard[randRow][randCol] = (randPiece[0], randPiece[1])

        # Count the randomized board value
        ts1, td1, qs1, qd1, rs1, rd1, bs1, bd1, ks1, kd1 = Checker.conflictChecker(tempBoard)
        tempValue = ts1 - td1
        
        # If the next state value is better, accept it
        if tempValue <= Value :
            bestResult = copy.deepcopy(tempBoard)
            Value = tempValue
            improved += 1
        # If the next state value is worse, accept with probability of it is higher than a random number
        elif tempValue > Value :
            sigmoidFunc = math.floor(math.exp(-T)) * 100
            randomNum = randint(0,100)
            if sigmoidFunc > randomNum :
                bestResult = copy.deepcopy(tempBoard)
                Value = tempValue
                accepted += 1
        
        # Iterator value decreased
        iterator -= 1

    # Result of improved states
    print(improved)
    # Result of accepted states
    print(accepted)
    return bestResult

