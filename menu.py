from IO import Printer
from Algorithms import BoardHandler
from Algorithms import Genetic
from Algorithms import hc
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
     "Credit",
     "Exit"
    ]


def colorize(string, color):
    if not color in colors:
        return string

    return colors[color] + string + '\033[0m'


def credit():
    S =\
    """
    >> Created by:
    >>   Kevin Leonardo Limitius    13516049    Aku adalah Istriku Documenter
    >>   Christian Kevin Saputra    13516073    Genetic Algorithm Pioneer
    >>   Tanor Abraham Reyuko       13516088    Simulated Annealing Expert
    >>   Ahmad Faishol Huda         13516094    Hill Climber
    >>   Shandy                     13516097    Main Menu Man, Board Lover, Conflict Searcher
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
                Printer.printChessBoard(chessBoard)
            elif choice == 6:
                Genetic.GeneticAlgorithm(BoardHandler.createPiecesList(chessBoard))
            elif choice == 7:
                credit()
            elif choice == 8:
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
