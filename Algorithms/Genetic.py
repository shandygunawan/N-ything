from Algorithms import BoardHandler, Checker
from IO import Printer, Parser
from random import randint,choice
import copy, time

maxPopulation = 100 # max population
maxGeneration = 300 # max loop

class Chromosome() :

	def __init__(self) :
		self.board = []
		self.piecesLocation = []
		self.fitness = 0


def initialize_population(chessList): # initialize the population
	population = []
	for i in range(100) :
		chromosome = Chromosome()
		chromosome.board = []
		chromosome.piecesLocation = BoardHandler.random_genetic(chromosome.board, chessList)
		conflict = Checker.conflictChecker(chromosome.board)
		chromosome.fitness = conflict[0] - conflict[1]
		population.append(chromosome)

	populationSort(population) # sort population by highest fit
	deleteLeastFit(population) # delete half of least fit population

	return population

def getFitness(chromosome) : # function to help sort by chromosome fitness
	return chromosome.fitness

def populationSort(population) : # sort population from best fit to least fit
	population.sort(key=getFitness)

def getParents(population, index) : # get parents from the surviving population
	parent1 = population[index]
	parent2 = population[index + 1]
	return parent1, parent2

def deleteLeastFit(population) : # remove the  least fit chromosome from population so that only half of the population remaining
	del population[int(maxPopulation/2):]

def checkDouble(chromosome): # check is there are any piece in same location
	for i in range(len(chromosome.piecesLocation) - 1):
		for j in range(i+1, len(chromosome.piecesLocation)) :
			if(chromosome.piecesLocation[i][0] == chromosome.piecesLocation[j][0]) :
				return True

	return False

def listDouble(chromosome): # list all pieces that are in same location
	double = []
	for i in range(len(chromosome.piecesLocation)):
		if i < (len(chromosome.piecesLocation)-1):
			a = i + 1
		else:
			double = list(set(double))
			return double
		for j in range (a,len(chromosome.piecesLocation)):
			if chromosome.piecesLocation[i][0] == chromosome.piecesLocation[j][0]:
				double.append(i)
				double.append(j)
	double = list(set(double))
	return double

def crossOver(newGeneration, parent1, parent2) : #reproduce new chromosome 
	crossBorder = randint(1, len(parent1.piecesLocation) - 1) # border to determine how many piece will be swap

	child1 = copy.deepcopy(parent1)
	child2 = copy.deepcopy(parent2)

	for i in range(crossBorder) :
		temp = child1.piecesLocation[i]
		child1.piecesLocation[i] = child2.piecesLocation[i]
		child2.piecesLocation[i] = temp

	if checkDouble(child1): 
		mutationDouble(child1)
		
	if checkDouble(child2):
		mutationDouble(child2)

	mutationConstant = randint(1,10) 
	if (mutationConstant > 3) : #have 70% chance of mutation
		if (randint(1,2) == 1) :
			mutation(child1)
		else :
			mutation(child2)
		
	updateBoardandFitness(child1)
	updateBoardandFitness(child2)
	newGeneration.append(child1)
	newGeneration.append(child2)

def mutation(child) : # normal mutation function 
	BoardHandler.updateBoard(child.board, child.piecesLocation)
	member = randint(0,len(child.piecesLocation)-1) # choose piece to mutate
	row = randint(0,7)
	col = randint(0,7)
	while child.board[row][col] != ('.',".") :
		row = randint(0,7)
		col = randint(0,7)
	
	child.piecesLocation[member][0][0] = row
	child.piecesLocation[member][0][1] = col

def mutationDouble(child) : # mutation function if there are some positions that clash
	BoardHandler.updateBoard(child.board, child.piecesLocation)

	while checkDouble(child):
		double = listDouble(child)
		member = choice(double)
	
		row = randint(0,7)
		col = randint(0,7)

		while child.board[row][col] != ('.',".") :
			row = randint(0,7)
			col = randint(0,7)
	
		child.piecesLocation[member][0][0] = row
		child.piecesLocation[member][0][1] = col

def updateBoardandFitness(child) : #update chromosome board and fitness score after cross over
	BoardHandler.updateBoard(child.board, child.piecesLocation)
	conflict = Checker.conflictChecker(child.board)
	child.fitness = conflict[0] - conflict[1] 

def GeneticAlgorithm(chessList): # the process of genetic algorithm
	population = initialize_population(chessList)
	generationCount = 1
	count = 1
	maxFitness = 0

	while (generationCount <= maxGeneration) :
		newGeneration = []
		index = 0
		while index < (maxPopulation/2 - 1) :
			parent1 , parent2 = getParents(population, index)
			crossOver(newGeneration,parent1, parent2)
			index = index + 1
		population = newGeneration + population # add new generation to current population
		populationSort(population)
		deleteLeastFit(population)
		print("Generation :" + str(generationCount) + ", Fittest : ", abs(population[0].fitness))
		if (population[0].fitness != maxFitness) :
			maxFitness = population[0].fitness
			count = 1
		else :
			count += 1

		if(count == 100): # if in 100 gen there is no change in fittest score
			print("Same fitness for " + str(count) + " gen")
			print("Terminate")
			time.sleep(1)
			break
		else:
			generationCount = generationCount + 1

	# print (population[0].piecesLocation)
	if (generationCount == maxGeneration) :
		print("Max iteration reach")
		time.sleep(1)
	Printer.printChessBoard(population[0].board)
	Printer.printSolutionToFile(population[0].board, "Genetic")


# chessList = Parser.readPiecesFile("Inputs/" + input(">> Enter filename: "))
# GeneticAlgorithm(chessList)
