from IO import Printer
from Algorithms import BoardHandler
from Algorithms import Genetic
from Algorithms import hc
from Algorithms import SimulatedAnnealing
import os

header = "\
_________               .__    __________                   __               __\n\
\_   ___ \  ____   ____ |  |   \______   \_______  ____    |__| ____   _____/  |_\n\
/    \  \/ /  _ \ /  _ \|  |    |     ___/\_  __ \/  _ \   |  |/ __ \_/ ___\   __\\\n\
\     \___(  <_> |  <_> )  |__  |    |     |  | \(  <_> )  |  \  ___/\  \___|  |\n\
 \______  /\____/ \____/|____/  |____|     |__|   \____/\__|  |\___  >\___  >__|\n\
        \/                                             \______|    \/     \/      \n"


colors = {
    'blue': '\033[94m',
    'pink': '\033[95m',
    'green': '\033[92m',
}

menuItems =\
    ["Create a new Chess board from pieces",
     "Read a chess board",
     "Show the Chess board",
     "Solve with Hill-Climbing",
     "Solve with Simulated Annealing",
     "Solve with Genetic Algorithm",
     "Help Me",
     "Credit",
     "Exit"]


def colorize(string, color):
    if color not in colors:
        return string

    return colors[color] + string + '\033[0m'


def credit():
    S = """
    >> Created by:
    >>   Kevin Leonardo Limitius    13516049    Aku adalah Istriku Documenter
    >>   Christian Kevin Saputra    13516073    Genetic Algorithm Pioneer
    >>   Tanor Abraham Reyuko       13516088    Simulated Annealing Expert
    >>   Ahmad Faishol Huda         13516094    Hill Climber
    >>   Shandy                     13516097    Main Menu Man, Board Lover, Conflict Searcher
    """
    print(S)


def helpMe():
    S = """
    >> HELP:
    >> 1. Created a new chess Board from pieces:
    >>      -> Program will create a random chess board based on pieces information.
    >>      -> Use files named 'Pieces<number>.txt' as input from 'Inputs' folder."
    >>      -> Using this options will overwrite previously created/loaded chess board.
    >>
    >> 2. Read a chess board:
    >>      -> Program will read a chess board input and use it.
    >>      -> Use files named 'Board<number>.txt' as input from 'Inputs' folder."
    >>      -> Using this options will overwrite previously created/loaded chess board.
    >>
    >> 3. Show the chess board:
    >>      -> Program will display chess board created from option 1 or loaded from option 2
    >>      -> Total conflict A and B also displayed.
    >>      -> Conflict A : Conflict between chess pieces with same color
    >>      -> Conflict B : Conflict between chess pieces with different color
    >>
    >> 4. Solve with Hill-Climbing
    >>      -> Solve created or loaded chess board with hill-climbing algorithm.
    >>
    >> 5. Solve with Simulated Annealing
    >>      -> Solve created or loaded chess board with Simulated Annealing algorithm.
    >>
    >> 6. Solve with Genetic Algorithm
    >>      -> Solve created or loaded chess board with genetic algorithm.
    >>
    >> 7. Help Me
    >>      -> Shows information to help first-time users.
    >>      -> Literally texts that you are reading right now.
    >>
    >> 8. Credit
    >>      -> A group of remarkable people to fight the battle that you never could.
    >>
    >> 9. Exit
    >>      -> Sayonara. Please watch an anime if you haven't today, you won't regret it.
    >>
    >>
    >> NOTE:
    >> -> Option 4, 5, 6 will output a result in 'Solutions' folder.
    >> -> Option 4, 5, 6 don't change loaded or created chess board state from the initial state. 
    """
    print(S)


def mainMenu():
    chessBoard = []
    while True:
        if os.name == 'nt':  # Windows
            os.system('cls')
        elif os.name == 'posix':  # Linux
            os.system('clear')

        print(colorize(header, 'pink'))
        i = 1
        for item in menuItems:
            print("[" + str(i) + "] " + colorize(item, 'blue'))
            i += 1

        choice = int(input(">> "))

        try:
            if choice < 1:
                raise ValueError

            # Call the matching function
            if choice == 1:
                Printer.printDir("Inputs/")
                chessBoard = BoardHandler.createChessboard()
            elif choice == 2:
                Printer.printDir("Inputs/")
                chessBoard = BoardHandler.readChessboard()
            elif choice == 3:
                Printer.printChessBoard(chessBoard)
            elif choice == 4:
                maxTry = int(input(">> Enter maximum try : "))
                Printer.printChessBoard(hc.hillC(maxTry, chessBoard))
            elif choice == 5:
                maxTry = int(input(">> Enter maximum try : "))
                Printer.printChessBoard(SimulatedAnnealing.simulatedAnnealing(maxTry, chessBoard))
            elif choice == 6:
                Genetic.GeneticAlgorithm(BoardHandler.createPiecesList(chessBoard))
            elif choice == 7:
                helpMe()
            elif choice == 8:
                credit()
            elif choice == 9:
                exit(0)
            else:
                print(">> That is not a valid input.")
        except (ValueError, IndexError):
            pass

        while True:
            text = input("\n>> Press enter to continue.")
            if text == "":
                break
            else:
                print("\n>> You did not press enter.")

        print("\n\n")
