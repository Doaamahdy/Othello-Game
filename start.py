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
#color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 120, 0)

easy_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2, 100, 50)
medium_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 100, 100, 50)
hard_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 200, 100, 50)

class gameController:
    def __init__(self, win):
        self.resetWindow()
        self.win = win
        self.findWin = False
        self.level = None

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
    
    def computerMove(self, row, col):

        self.board.printAllValidMoves(self.turn) 
        pygame.time.delay(2000) 
        row,col = getBestMove(self.board,self.level)
        self.makeMove(row, col)
        self.takeTurns()

       
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
    game = gameController(screen)

    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            #if wana exist the game   
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #if find winner set findWin to true to stop the game and 
            elif game.board.findWinner():
                  game.findWin = True

            #if the current player doesnot have any moves to make                                      
            elif game.board.getAllValidMoves(game.turn) == [] and game.findWin == False:
                game.takeTurns()
            #if it is the computer's turn make computer plays
            elif  game.turn == WHITE and game.findWin == False:
                game.computerMove(row, col)
            # if the player click on any cell on the board            
            elif event.type == pygame.MOUSEBUTTONDOWN and game.findWin == False:
                mouse_pos = pygame.mouse.get_pos()
                               
                if easy_button.collidepoint(mouse_pos) and game.level == None:
                    game.level = 1

                elif medium_button.collidepoint(mouse_pos)and game.level == None:
                    game.level = 3

                elif hard_button.collidepoint(mouse_pos)and game.level == None:
                    game.level = 5

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button clicked
                        mouse_pos = pygame.mouse.get_pos()
                        row, col = game.board.get_clicked_position(mouse_pos)
                        game.board.printAllValidMoves(game.turn)                                     
                        if game.makeMove(row, col):                           
                            game.takeTurns()
                            game.board.drawBoard(screen,game.turn)                                                                                
                            print("Move made successfully")
                        else:
                            print("Invalid move")


        if game.level == None:
            draw_menu(screen)
        else:    
            game.board.drawBoard(screen,game.turn, game.findWin)


if __name__ == "__main__":
    main()


