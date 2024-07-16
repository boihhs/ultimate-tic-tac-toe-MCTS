from nodeAlgo import Node
from ultimatetictactoe import UltimateTicTacToe
import random
from ultimateictactoeguiclass import UTTTGUI
import time
    

totalGames = 0.0
totalWinsAI = 0.0
points = .5


for i in range(20):
    
    boardMain = UltimateTicTacToe()
    
    while(boardMain.isTerminal()[0] == False):
        test = Node(None, boardMain)
        for i in range(10000):
            test.MCTS()
        boardMain = test.finalSelection().board
        print("X: " + str(test.finalSelection().totalWins/test.finalSelection().totalSims))
        if boardMain.isTerminal()[0] == False:
            test = Node(None, boardMain)
            for i in range(10000):
                test.MCTS()
            boardMain = test.finalSelection().board
            print("O: " + str(test.finalSelection().totalWins/test.finalSelection().totalSims))
       
    boardMain.printBoard()
        
    totalGames = totalGames + 1
    if boardMain.winner == None:
        points =  .5
    elif boardMain.winner == 10:
        points =  1
    else: points =  0
    totalWinsAI = totalWinsAI + points
    print("win % " + str(totalWinsAI/totalGames))

print(totalWinsAI/totalGames)
    
    




    