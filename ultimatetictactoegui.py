import pygame
import sys
from ultimatetictactoe import UltimateTicTacToe


# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 9, 9
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 10
SPACE = SQUARE_SIZE // 4
# RGB colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (200, 0, 0)
BLACK = (30, 30, 30)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The ULTIMATE Tic Tac Toe")
screen.fill(BG_COLOR)

def draw_grid():
    for row in range(1, BOARD_ROWS):
        if row % 3 != 0: pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
        
        
    for col in range(1, BOARD_COLS):
        if col % 3 != 0: pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        
    for row in range(1, BOARD_ROWS):
        if row % 3 == 0:
            pygame.draw.line(screen, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH-5)
        
    for col in range(1, BOARD_COLS):
        if col % 3 == 0:
            pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH-5)
        

def draw_x(row, col):
    x_pos = col * SQUARE_SIZE
    y_pos = row * SQUARE_SIZE
    pygame.draw.line(screen, CROSS_COLOR, (x_pos + SPACE, y_pos + SQUARE_SIZE - SPACE), (x_pos + SQUARE_SIZE - SPACE, y_pos + SPACE), CROSS_WIDTH)
    pygame.draw.line(screen, CROSS_COLOR, (x_pos + SPACE, y_pos + SPACE), (x_pos + SQUARE_SIZE - SPACE, y_pos + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def drawBig_x(row, col):
    x_pos = col * SQUARE_SIZE * 3
    y_pos = row * SQUARE_SIZE * 3
    pygame.draw.line(screen, CROSS_COLOR, (x_pos + SPACE* 3 , y_pos + (SQUARE_SIZE - SPACE) * 3), (x_pos + (SQUARE_SIZE - SPACE) * 3, y_pos + SPACE * 3), CROSS_WIDTH * 3)
    pygame.draw.line(screen, CROSS_COLOR, (x_pos + SPACE * 3, y_pos + SPACE * 3), (x_pos + (SQUARE_SIZE - SPACE) * 3, y_pos + (SQUARE_SIZE - SPACE) * 3), CROSS_WIDTH * 3)

def drawBigBig_x(row, col):
    x_pos = col * SQUARE_SIZE * 9
    y_pos = row * SQUARE_SIZE * 9
    pygame.draw.line(screen, CROSS_COLOR, (x_pos + SPACE* 9 , y_pos + (SQUARE_SIZE - SPACE) * 9), (x_pos + (SQUARE_SIZE - SPACE) * 9, y_pos + SPACE * 9), CROSS_WIDTH * 9)
    pygame.draw.line(screen, CROSS_COLOR, (x_pos + SPACE * 9, y_pos + SPACE * 9), (x_pos + (SQUARE_SIZE - SPACE) * 9, y_pos + (SQUARE_SIZE - SPACE) * 9), CROSS_WIDTH * 9)

def draw_o(row, col):
    x_pos = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y_pos = row * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.circle(screen, CIRCLE_COLOR, (x_pos, y_pos), CIRCLE_RADIUS, CROSS_WIDTH)

def drawBig_o(row, col):
    x_pos = (col * SQUARE_SIZE + SQUARE_SIZE // 2) * 3
    y_pos = (row * SQUARE_SIZE + SQUARE_SIZE // 2) * 3
    pygame.draw.circle(screen, CIRCLE_COLOR, (x_pos, y_pos), CIRCLE_RADIUS * 3, CROSS_WIDTH * 3)

def drawBigBig_o(row, col):
    x_pos = (col * SQUARE_SIZE + SQUARE_SIZE // 2) * 9
    y_pos = (row * SQUARE_SIZE + SQUARE_SIZE // 2) * 9
    pygame.draw.circle(screen, CIRCLE_COLOR, (x_pos, y_pos), CIRCLE_RADIUS * 9, CROSS_WIDTH * 9)


running = True

board = UltimateTicTacToe()
def getNumBoard(row,col):
    cordToNumb = {(0,0): 0, (0,1): 1, (0,2): 2, (1,0): 3, (1,1): 4, (1,2): 5, (2,0): 6, (2,1): 7, (2,2): 8}
    cord = (int((row)/3),int((col)/3))
    return cordToNumb[cord]

def getNumSquare(row,col):
    cordToNumb = {(0,0): 8, (0,1): 6, (0,2): 7, (1,0): 2, (1,1): 0, (1,2): 1, (2,0): 5, (2,1): 3, (2,2): 4}
    cord = (int((row+1)%3),int((col+1)%3))
    return cordToNumb[cord]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            board.makeMove((getNumBoard(clicked_row, clicked_col), getNumSquare(clicked_row, clicked_col)))
            
            
            

    screen.fill(BG_COLOR)
    draw_grid()
    bigArray = board.convertToBigArray()
    
    for i in range(len(bigArray)):
        if(bigArray[i] == 10):
            draw_x(int(i/9), i%9)
        if(bigArray[i] == 5):
            draw_o(int(i/9), i%9)
    for i in range(len(board.board)):
        if (board.board[i]).winner == 10:
            drawBig_x(int(i/3), i%3)
    for i in range(len(board.board)):
        if (board.board[i]).winner == 5:
            drawBig_o(int(i/3), i%3)
    if board.winner == 10:
        drawBigBig_x(0,0)
    if board.winner == 5:
        drawBigBig_o(0,0)
    pygame.display.update()