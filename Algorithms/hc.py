from Algorithms import Checker
from IO import Printer
import copy

	
# Generate all the neighbour and pick best neighbour	
def getBestNeighbour(chessboard):
	counter = 0
	size = len(chessboard)
	
	# Initial Chessboard
	
	BestNeighbour = copy.deepcopy(chessboard)
	ts0, td0, qs0, qd0, rs0, rd0, bs0, bd0, ks0, kd0 = Checker.conflictChecker(BestNeighbour)
	Value = ts0-td0
	# Printer.printChessBoard(BestNeighbour)
	for row in range(size):
		for col in range(size):
		
			# If there is a piece in this box, then move it
			if chessboard[row][col] != ('.', "."):
				
				# Iterate all box in board, search for empty box
				for rowIter in range(size):
					for colIter in range(size):
						
						# If found an empty box, move piece to the empty box
						if chessboard[rowIter][colIter] == ('.', "."):
							counter += 1
							chessboard[rowIter][colIter] = chessboard[row][col]
							chessboard[row][col] = ('.', ".")
							
							# Printer.printChessBoard(chessboard)
							
							# Check value of current state and compare it with BestNeighbour
							ts1, td1, qs1, qd1, rs1, rd1, bs1, bd1, ks1, kd1 = Checker.conflictChecker(chessboard)
							ValueNeighbour = ts1-td1
							if ValueNeighbour <= Value:
								BestNeighbour = copy.deepcopy(chessboard)
								Value = ValueNeighbour
							# Printer.printChessBoard(BestNeighbour)
							# Reset board to initial board
							chessboard[row][col] = chessboard[rowIter][colIter]
							chessboard[rowIter][colIter] = ('.', ".")
	return BestNeighbour


# Return deviation of Value Current state and its best neighbour	
def evaluate(Neigbour, currentState):
	ts1, td1, qs1, qd1, rs1, rd1, bs1, bd1, ks1, kd1 = Checker.conflictChecker(Neigbour)
	ts2, td2, qs2, qd2, rs2, rd2, bs2, bd2, ks2, kd2 = Checker.conflictChecker(currentState)
	t1 = ts1 - td1
	t2 = ts2 - td2
	return t1 - t2


# Hill Climbing Algorithm
def hillC(maxTry, chessboard):
	# Generate initial state
	currentState = copy.deepcopy(chessboard)
	# Iterate Try times
	for i in range(maxTry):
		print(i)
		bestNeighbour = copy.deepcopy(getBestNeighbour(currentState))
		
		# Compare current state with best neighbour, if current state is better return current state, 
		if evaluate(bestNeighbour, currentState) > 0:
			Printer.printChessBoard(currentState)
			Printer.printSolutionToFile(currentState, "HillClimbing")
			return currentState
		Printer.printChessBoard(currentState)
		# else assign current state with best neighbour
		currentState = copy.deepcopy(bestNeighbour)
	
	# Return current state if function HC cannot find maximum until try times
	Printer.printChessBoard(currentState)
	Printer.printSolutionToFile(currentState, "HillClimbing")
	return currentState
