import pygame
import sys
from ultimatetictactoe import UltimateTicTacToe
import random
from nodeAlgo import Node

class UTTTGUI:
    
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        self.board = UltimateTicTacToe()
        self.clock = pygame.time.Clock()
        self.is_running = True

        # Constants
        self.WIDTH, self.HEIGHT = 600, 600
        self.LINE_WIDTH = 15
        self.BOARD_ROWS, self.BOARD_COLS = 9, 9
        self.SQUARE_SIZE = self.WIDTH // self.BOARD_COLS
        self.CIRCLE_RADIUS = self.SQUARE_SIZE // 3
        self.CIRCLE_WIDTH = 10
        self.CROSS_WIDTH = 10
        self.SPACE = self.SQUARE_SIZE // 4
        # RGB colors
        self.BG_COLOR = (28, 170, 156)
        self.LINE_COLOR = (23, 145, 135)
        self.CIRCLE_COLOR = (239, 231, 200)
        self.CROSS_COLOR = (200, 0, 0)
        self.BLACK = (30, 30, 30)

        # Create the screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("The ULTIMATE Tic Tac Toe")
        self.screen.fill(self.BG_COLOR)

    def draw_grid(self):
        for row in range(1, self.BOARD_ROWS):
            if row % 3 != 0: pygame.draw.line(self.screen, self.LINE_COLOR, (0, row * self.SQUARE_SIZE), (self.WIDTH, row * self.SQUARE_SIZE), self.LINE_WIDTH)
            
            
        for col in range(1, self.BOARD_COLS):
            if col % 3 != 0: pygame.draw.line(self.screen, self.LINE_COLOR, (col * self.SQUARE_SIZE, 0), (col * self.SQUARE_SIZE, self.HEIGHT), self.LINE_WIDTH)
            
        for row in range(1, self.BOARD_ROWS):
            if row % 3 == 0:
                pygame.draw.line(self.screen, self.BLACK, (0, row * self.SQUARE_SIZE), (self.WIDTH, row * self.SQUARE_SIZE), self.LINE_WIDTH-5)
            
        for col in range(1, self.BOARD_COLS):
            if col % 3 == 0:
                pygame.draw.line(self.screen, self.BLACK, (col * self.SQUARE_SIZE, 0), (col * self.SQUARE_SIZE, self.HEIGHT), self.LINE_WIDTH-5)
            

    def draw_x(self, row, col):
        x_pos = col * self.SQUARE_SIZE
        y_pos = row * self.SQUARE_SIZE
        pygame.draw.line(self.screen, self.CROSS_COLOR, (x_pos + self.SPACE, y_pos + self.SQUARE_SIZE - self.SPACE), (x_pos + self.SQUARE_SIZE - self.SPACE, y_pos + self.SPACE),self.CROSS_WIDTH)
        pygame.draw.line(self.screen, self.CROSS_COLOR, (x_pos + self.SPACE, y_pos + self.SPACE), (x_pos + self.SQUARE_SIZE - self.SPACE, y_pos + self.SQUARE_SIZE - self.SPACE), self.CROSS_WIDTH)

    def drawBig_x(self, row, col):
        x_pos = col * self.SQUARE_SIZE * 3
        y_pos = row * self.SQUARE_SIZE * 3
        pygame.draw.line(self.screen, self.CROSS_COLOR, (x_pos + self.SPACE* 3 , y_pos + (self.SQUARE_SIZE - self.SPACE) * 3), (x_pos + (self.SQUARE_SIZE - self.SPACE) * 3, y_pos + self.SPACE * 3), self.CROSS_WIDTH * 3)
        pygame.draw.line(self.screen, self.CROSS_COLOR, (x_pos + self.SPACE * 3, y_pos + self.SPACE * 3), (x_pos + (self.SQUARE_SIZE - self.SPACE) * 3, y_pos + (self.SQUARE_SIZE - self.SPACE) * 3), self.CROSS_WIDTH * 3)

    def drawBigBig_x(self, row, col):
        x_pos = col * self.SQUARE_SIZE * 9
        y_pos = row * self.SQUARE_SIZE * 9
        pygame.draw.line(self.screen, self.CROSS_COLOR, (x_pos + self.SPACE* 9 , y_pos + (self.SQUARE_SIZE - self.SPACE) * 9), (x_pos + (self.SQUARE_SIZE - self.SPACE) * 9, y_pos + self.SPACE * 9), self.CROSS_WIDTH * 9)
        pygame.draw.line(self.screen, self.CROSS_COLOR, (x_pos + self.SPACE * 9, y_pos + self.SPACE * 9), (x_pos + (self.SQUARE_SIZE - self.SPACE) * 9, y_pos + (self.SQUARE_SIZE - self.SPACE) * 9), self.CROSS_WIDTH * 9)

    def draw_o(self, row, col):
        x_pos = col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
        y_pos = row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
        pygame.draw.circle(self.screen, self.CIRCLE_COLOR, (x_pos, y_pos), self.CIRCLE_RADIUS, self.CROSS_WIDTH)

    def drawBig_o(self, row, col):
        x_pos = (col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2) * 3
        y_pos = (row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2) * 3
        pygame.draw.circle(self.screen, self.CIRCLE_COLOR, (x_pos, y_pos), self.CIRCLE_RADIUS * 3, self.CROSS_WIDTH * 3)

    def drawBigBig_o(self, row, col):
        x_pos = (col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2) * 9
        y_pos = (row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2) * 9
        pygame.draw.circle(self.screen, self.CIRCLE_COLOR, (x_pos, y_pos), self.CIRCLE_RADIUS * 9, self.CROSS_WIDTH * 9)


    running = True

    
    def getNumBoard(self, row,col):
        cordToNumb = {(0,0): 0, (0,1): 1, (0,2): 2, (1,0): 3, (1,1): 4, (1,2): 5, (2,0): 6, (2,1): 7, (2,2): 8}
        cord = (int((row)/3),int((col)/3))
        return cordToNumb[cord]

    def getNumSquare(self, row,col):
        cordToNumb = {(0,0): 8, (0,1): 6, (0,2): 7, (1,0): 2, (1,1): 0, (1,2): 1, (2,0): 5, (2,1): 3, (2,2): 4}
        cord = (int((row+1)%3),int((col+1)%3))
        return cordToNumb[cord]
    
    def handle_events_random(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN and self.board.turn == 5:
                allMoves = self.board.generateMoves()
                chosenMove = random.choice(allMoves)
                
                self.board.makeMove(chosenMove)
            elif event.type == pygame.MOUSEBUTTONDOWN and self.board.turn == 10: 
                self.makeMCTSMove()

    def handle_events_MCTS(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.makeMCTSMove()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                if event.type == pygame.MOUSEBUTTONDOWN and self.board.turn == 5:
                    clicked_row = mouseY // self.SQUARE_SIZE
                    clicked_col = mouseX // self.SQUARE_SIZE
                    self.board.makeMove((self.getNumBoard(clicked_row, clicked_col), self.getNumSquare(clicked_row, clicked_col)))
                        
                    
                elif event.type == pygame.MOUSEBUTTONDOWN and self.board.turn == 10: 
                    self.makeMCTSMove()
                
    
    def changeBoard(self, newBoard):
        self.board = newBoard

    def render(self):
        self.screen.fill(self.BG_COLOR)
        self.draw_grid()
        bigArray = self.board.convertToBigArray()
        
        for i in range(len(bigArray)):
            if(bigArray[i] == 10):
                self.draw_x(int(i/9), i%9)
            if(bigArray[i] == 5):
                self.draw_o(int(i/9), i%9)
        for i in range(len(self.board.board)):
            if (self.board.board[i]).winner == 10:
                self.drawBig_x(int(i/3), i%3)
        for i in range(len(self.board.board)):
            if (self.board.board[i]).winner == 5:
                self.drawBig_o(int(i/3), i%3)
        if self.board.winner == 10:
            self.drawBigBig_x(0,0)
        if self.board.winner == 5:
            self.drawBigBig_o(0,0)
        pygame.display.update()

    def makeMCTSMove(self):
        test = Node(None, self.board)
        for i in range(1000):
            test.MCTS()
        for i in range(len(test.children)):
            print("wins: " + str(test.children[i].totalWins) + "; sim: " + str(test.children[i].totalSims) + "; %: " + str(test.children[i].totalWins/test.children[i].totalSims))
        print("\n\n\n")
        self.board = test.finalSelection().board

    def run(self):
        while self.is_running:
            self.handle_events()
            #self.update()
            self.render()
            self.clock.tick(60)  # Limit frame rate to 60 FPS

        pygame.quit()
        sys.exit()
    
     

if __name__ == "__main__":
    game = UTTTGUI()
    game.run()