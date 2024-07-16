
class TicTacToe():
    EMPTY = 0
    O = 5
    X = 10

    def __init__(self):

        self.board = [self.EMPTY, self.EMPTY, self.EMPTY,
                      self.EMPTY, self.EMPTY, self.EMPTY,
                      self.EMPTY, self.EMPTY, self.EMPTY ]
        
        self.turn = self.X

        self.legalMoves = None

        self.winner = None
    
    def generateMoves(self):
        moves = []
        for i in range(len(self.board)):
            if self.board[i] == self.EMPTY:
                moves.append(i)
        self.legalMoves = moves
        return self.legalMoves
    
    def isTerminal(self):
        
        for i in range(0,7, 3):
            if (self.board[i]*self.board[i+1]*self.board[i+2] == 125 or self.board[i]*self.board[i+1]*self.board[i+2] == 1000):
                self.winner = self.board[i]
                return (True, self.board[i])
                
        for i in range(3):
            if (self.board[i]*self.board[i+3]*self.board[i+6] == 125 or self.board[i]*self.board[i+3]*self.board[i+6] == 1000):
                self.winner = self.board[i]
                return (True, self.board[i])

        if self.board[0]*self.board[4]*self.board[8] == 125 or self.board[0]*self.board[4]*self.board[8] == 1000:
            self.winner = self.board[0]
            return (True, self.board[0])
        
        if self.board[2]*self.board[4]*self.board[6] == 125 or self.board[2]*self.board[4]*self.board[6] == 1000:
            self.winner = self.board[2]
            return (True, self.board[2])
        
        for i in range(len(self.board)):
            if self.board[i] == self.EMPTY:
                return (False, None)
            
        return (True, None)
    
    def makeMove(self, square, xOrO):
        if square in self.generateMoves():
            self.board[square] = xOrO
            #self.isTerminal()
    
    def printBoard(self):
        boardToXO = {
        "5" : "O",
        "10" : "X",
        "0": " "
        }
        for a in range(0,7,3):
            for i in range(3):
                if i < 2: 
                    print(boardToXO[str(self.board[a+i])] + " | ", end="")
                else:
                    print(boardToXO[str(self.board[a+i])], end="")
            print("")
            if a <5: print("---------")

    def __mul__(self, other):
        #self.isTerminal()
        if isinstance(other, int):
            if self.winner == None:
                return 0
            else:
                return self.winner * other
        elif self.winner == None or other.winner == None:
            return 0
        else: return self.winner * other.winner

    

                



