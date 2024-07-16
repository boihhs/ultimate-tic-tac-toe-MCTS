from ultimatetictactoe import UltimateTicTacToe
import random
import copy
import math

class Node:
    
    def __init__(self, parent, board):
        self.totalWins = 0.0
        self.totalSims = 0.0
        self.parent = parent
        self.children = []
        self.board = board

    def expansion(self):
        allMoves = self.board.generateMoves()
        
        for i in range(len(allMoves)):
            copys = copy.deepcopy(self.board)
            copys.makeMove(allMoves[i])
            self.children.append(Node(self, copys))
    
    def getUTCValue(self):
        return (self.totalWins/self.totalSims) + math.sqrt(2)*math.sqrt(math.log(self.parent.totalSims, math.e)/self.totalSims)
    
    def selection(self):
        
        max = 0
        maxValue = 0
        
        for i in range(len(self.children)):
            if self.children[i].totalSims == 0:
                return self.children[i]
            if self.children[i].getUTCValue() > maxValue:
                maxValue = self.children[i].getUTCValue()
                max = i
        return self.children[max]
    
    def finalSelection(self):
        
        max = 0
        maxValue = 0
        
        for i in range(len(self.children)):
            
            if self.children[i].totalSims > maxValue:
                maxValue = self.children[i].totalSims
                max = i
        return self.children[max]
    
    def backprop(self, playout):
        self.totalSims = self.totalSims + 1
        self.totalWins = self.totalWins + playout
        if self.parent != None:
            self.parent.backprop(playout)
    
    def isTerminal(self, turn):
        if self.board.isTerminal()[0]:
            end = self.board.isTerminal()[1]
            if turn == 10:
                if end == None:
                    return .5
                elif end == 10:
                    return 1
                else: return 0
            else:
                if end == None:
                    return .5
                elif end == 10:
                    return 0
                else: return 1
        

    def playout(self, turn):
        
        copys = copy.deepcopy(self.board)
        while copys.isTerminal()[0] == False:
            
            allMoves = copys.generateMoves()
            chosenMove = random.choice(allMoves)
            copys.makeMove(chosenMove)
        if turn == 10:
            if copys.winner == None:
                return .5
            elif copys.winner == 10:
                return 1
            else: return 0
        else:
            if copys.winner == None:
                return .5
            elif copys.winner == 10:
                return 0
            else: return 1
    
   

    def MCTS(self):
        node = self
        while len(node.children) != 0:
            node = node.selection()
        if node.totalSims == 0:
            if node.board.isTerminal()[0]:
                node.backprop(node.isTerminal(self.board.turn))
            else:
                node.backprop(node.playout(self.board.turn))
            return ""
        node.expansion()

        if node.board.isTerminal()[0]:
            node.backprop(node.isTerminal(self.board.turn))
        else:
            node = node.selection()
            node.backprop(node.playout(self.board.turn))




