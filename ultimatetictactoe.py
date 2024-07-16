from tictactoe import TicTacToe

class UltimateTicTacToe():
    EMPTY = 0
    O = 5
    X = 10

    def __init__(self):

        self.board = [TicTacToe(), TicTacToe(), TicTacToe(),
                      TicTacToe(), TicTacToe(), TicTacToe(),
                      TicTacToe(), TicTacToe(), TicTacToe() ]
        
        self.turn = self.X

        self.legalMoves = []
        
        self.lastMove = -1

        self.winner = None
    
    def generateMoves(self):
        allMoves = []
        moves = []
        if self.lastMove == -1:
            for i in range(len(self.board)):
                moves = self.board[i].generateMoves()
                for a in range(len(moves)):
                    allMoves.append((i,moves[a]))
            
        elif self.board[self.lastMove].winner != None:
            
            for i in range(len(self.board)):
                if self.board[i].winner == None:
                    moves = self.board[i].generateMoves()
                    for a in range(len(moves)):
                        allMoves.append((i,moves[a]))

        else:
            moves = self.board[self.lastMove].generateMoves()
            for a in range(len(moves)):
                allMoves.append((self.lastMove,moves[a]))
        
        self.legalMoves = allMoves
        return self.legalMoves
    
    def isTerminal(self):
        if len(self.generateMoves()) == 0:
            return (True, None)
        for i in range(0,7, 3):
            if (self.board[i]*(self.board[i+1]*self.board[i+2]) == 125 or self.board[i]*(self.board[i+1]*self.board[i+2]) == 1000):
                self.winner = (self.board[i]).winner
                return (True, (self.board[i]).winner)
            
        for i in range(3):
            if (self.board[i]*(self.board[i+3]*self.board[i+6]) == 125 or self.board[i]*(self.board[i+3]*self.board[i+6]) == 1000):
                self.winner = (self.board[i]).winner
                return (True, (self.board[i]).winner)
            
        if self.board[0]*(self.board[4]*self.board[8]) == 125 or self.board[0]*(self.board[4]*self.board[8]) == 1000:
            self.winner = (self.board[0]).winner
            return (True, (self.board[0]).winner)
        
        if self.board[2]*(self.board[4]*self.board[6]) == 125 or self.board[2]*(self.board[4]*self.board[6]) == 1000:
            self.winner = (self.board[2]).winner
            return (True, (self.board[2]).winner)
        
        for a in range(len(self.board)):
            for b in range(len(self.board)):
                if self.board[a].board[b] == self.EMPTY:
                    return (False, None)
        return (True, None)
    
    def makeMove(self, square):
        
        if square in self.generateMoves():
            (self.board[square[0]]).board[square[1]] = self.turn
            if self.turn == self.X:
                self.turn = self.O
            else:
                self.turn = self.X
            self.lastMove = square[1]
            (self.board[square[0]]).isTerminal()
            self.isTerminal()
            
    def convertToBigArray(self):
        bigArray = []
        for a in range(0,7,3):
            for b in range(0,7,3):
                for c in range(3):
                    for d in range(3):
                        bigArray.append((self.board[c+a]).board[d+b])
        return bigArray
                        
    def printBigArray(self):
        bigArray = self.convertToBigArray()
        print(self.convertToBigArray())
        count = 0
        for a in range(9):
            for b in range(9):
                print(str(bigArray[count])+", ", end = "")
                count = count+1
            print("")

    def printBoard(self):
        boardToXO = {
        "5" : "O",
        "10" : "X",
        "0": " "
        }
        
        for a in range(0,7,3):
            for b in range(0,7,3):
                for c in range(3):
                    for d in range(3):
                        if (c+a+1)%3 == 0 and (b+d+1)%3 == 0: 
                            print(boardToXO[str((self.board[c+a]).board[d+b])], end="")
                        else: print(boardToXO[str((self.board[c+a]).board[d+b])] + " | ", end="")
                print("")
                print("--------- | --------- | ---------")
            print("")
    
    def toNetworkInput(self):
        posVec = []
        bigArray = self.convertToBigArray()
        for i in range(len(bigArray)):
            if bigArray[i] == 10:
                posVec.append(1)
            else: posVec.append(0)
        for i in range(len(bigArray)):
            if bigArray[i] == 5:
                posVec.append(1)
            else: posVec.append(0)
        for i in range(9):
            if self.turn == 10:
                posVec.append(1)
            else: posVec.append(0)
        return posVec
    
    


    def getNetworkOutputIndex(self, move):
        a = move[0]
        b = move[1]
        numb = int(b/3) * 9 + (b % 3) + (a % 3) * 3 + 1 + int(a/3) * 27
        return numb
