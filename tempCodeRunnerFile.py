import pygame
import sys
from pygame.locals import *

from disk import Disk
from board import Board
from utilities import getBestMove

# Constants

WIDTH, HEIGHT = 600, 660
ROWS, COLS = 8, 8
SEQUARE_HEIGHT = (HEIGHT - 60) // COLS
SEQUARE_HEIGHT = WIDTH // COLS
PADDING = 2  # Define the padding size between squares

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 120, 0)
GREY = (128, 128, 128)

easy_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2, 100, 50)
medium_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 100, 100, 50)
hard_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 200, 100, 50)

class gameController:
    def __init__(self, win):
        self.resetWindow()
        self.win = win
        self.findWin = False

    def resetWindow(self):
        self.board = Board()
        self.turn = BLACK
        self.selected = None

    def takeTurns(self):
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def makeMove(self, row, col):
        return self.board.makeMove(row,col,self.turn)

       

def draw_menu(screen):
    screen.fill(GREEN)
    font = pygame.font.Font(None, 36)
    text = font.render("Choose Level:", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, BLACK, easy_button)
    easy_text = font.render("Easy", True, WHITE)
    easy_text_rect = easy_text.get_rect(center=easy_button.center)
    screen.blit(easy_text, easy_text_rect)

    pygame.draw.rect(screen, BLACK, medium_button)
    medium_text = font.render("Medium", True, WHITE)
    medium_text_rect = medium_text.get_rect(center=medium_button.center)
    screen.blit(medium_text, medium_text_rect)

    pygame.draw.rect(screen, BLACK, hard_button)
    hard_text = font.render("Hard", True, WHITE)
    hard_text_rect = hard_text.get_rect(center=hard_button.center)
    screen.blit(hard_text, hard_text_rect)

    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Othlo')
    clock = pygame.time.Clock()
    run = True
    game = gameController(screen)

    disk = Disk(3, 3, WHITE)
    disk.getCordinates()
    game.board.board[3][3] = disk

    disk = Disk(3, 4, BLACK)
    disk.getCordinates()
    game.board.board[3][4] = disk

    disk = Disk(4, 3, BLACK)
    disk.getCordinates()
    game.board.board[4][3] = disk

    disk = Disk(4, 4, WHITE)
    disk.getCordinates()
    game.board.board[4][4] = disk
    game.board.getAllValidMoves(BLACK)

    menu_running = True
    level = None
    while menu_running:
        for event in pygame.event.get():
           
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif game.board.findWinner():
                  game.board.drawBoard(screen,game.turn,True)
                  game.findWin = True
                     
            
            elif game.board.getAllValidMoves(game.turn) == [] and game.turn == BLACK and game.findWin == False:
                game.takeTurns()

            elif  game.turn == WHITE and game.findWin == False:
                print("Computer moves")
                game.board.printAllValidMoves(game.turn) 
                pygame.time.delay(4000) 
                row,col = getBestMove(game.board,level)
                game.makeMove(row, col)
                game.takeTurns()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and game.findWin == False:
                mouse_pos = pygame.mouse.get_pos()
                               
                if easy_button.collidepoint(mouse_pos) and level == None:
                    level = 1

                elif medium_button.collidepoint(mouse_pos)and level == None:
                    level = 3

                elif hard_button.collidepoint(mouse_pos)and level == None:
                    level = 5

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button clicked
                        mouse_pos = pygame.mouse.get_pos()
                        row, col = game.board.get_clicked_position(mouse_pos)
                        print("Clicked on row:", row, "column:", col)

                        print("my moves")
                        game.board.printAllValidMoves(game.turn)                                     
                        if game.makeMove(row, col):                           
                            game.takeTurns()
                            game.board.drawBoard(screen,game.turn)                                                                                
                            print("Move made successfully")
                        else:
                            print("Invalid move")


        if level == None:
            draw_menu(screen)
        else:    
            game.board.drawBoard(screen,game.turn)




if __name__ == "__main__":
    main()


