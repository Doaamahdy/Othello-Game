import pygame
from pygame.locals import *

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SEQUARE_HEIGHT = HEIGHT  // COLS
SEQUARE_HEIGHT = WIDTH // COLS

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 120, 0)
GREY = (128, 128, 128)
PADDING = 2
class Disk:
    PADDING = 15

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0

    def setColor(self,color):
        self.color = color
    
 
    def getCordinates(self):
        self.x = SEQUARE_HEIGHT * self.col + SEQUARE_HEIGHT // 2
        self.y = SEQUARE_HEIGHT * self.row + SEQUARE_HEIGHT // 2
        self.y += 60
        self.x += PADDING * (self.col + 1)
        self.y += PADDING * (self.row + 1)

    def drawDisk(self, win):
        radius = SEQUARE_HEIGHT // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def checkColor(self, color):
        if (self.color == color):
            return True
        else:
            return False