import pygame
from pygame.locals import *

from disk import Disk

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SEQUARE_HEIGHT = HEIGHT // COLS
SEQUARE_WIDTH = WIDTH // COLS
PADDING = 2  # Define the padding size between squares

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 120, 0)
GREY = (128, 128, 128)


class Board:

    def __init__(self):
        self.board = self.create_board()
        self.player = 30
        self.computer = 30
        # star with four disks 2 whites and 2 blacks
        disk = Disk(3, 3, WHITE)
        disk.getCordinates()
        self.board[3][3] = disk

        disk = Disk(3, 4, BLACK)
        disk.getCordinates()
        self.board[3][4] = disk

        disk = Disk(4, 3, BLACK)
        disk.getCordinates()
        self.board[4][3] = disk

        disk = Disk(4, 4, WHITE)
        disk.getCordinates()
        self.board[4][4] = disk

    def create_board(self):
        board = []
        for _ in range(ROWS):
            row = []
            for _ in range(COLS):
                row.append(None)  # Initialize each cell with None (no disk)
            board.append(row)
        return board

    def get_clicked_position(self, mouse_pos):
        x, y = mouse_pos
        y = y - 60
        col = x // (SEQUARE_WIDTH + PADDING)
        row = y // (SEQUARE_HEIGHT + PADDING)
        return row, col

    def drawBoard(self, win, turn, isWinner=False):
        win.fill(BLACK)

        # Draw turn text above the grid
        font = pygame.font.Font(None, 24)
        turn_text = font.render(
            f"Player's Turn: {'BLACK' if turn == BLACK else 'WHITE'}", True, GREEN)
        # Position the text at the top center
        turn_text_rect = turn_text.get_rect(midtop=(WIDTH // 2, 10))
        win.blit(turn_text, turn_text_rect)

    def drawValidMoves(self, color):
        validMoves = []
        for i in range(ROWS):
            for j in range(COLS):
                if self.checkValidMove(i, j, color):
                    validMoves.append([i, j])
        return validMoves

    def drawBoard(self, win, turn, isWinner=False):
        blacks, whites = self.getNumberOfDisks()
        win.fill(BLACK)

        # Draw turn text above the grid
        font = pygame.font.Font(None, 24)
        turn_text = font.render(
            f"Player's Turn: {'BLACK' if turn == BLACK else 'WHITE' } |  player: {self.player} computer :{self.computer}", True, GREEN)
        # Position the text at the top center
        turn_text_rect = turn_text.get_rect(midtop=(WIDTH // 2, 10))
        win.blit(turn_text, turn_text_rect)

        validMoves = self.drawValidMoves(turn)

        # Draw grid
        for row in range(ROWS):
            for col in range(COLS):
                rect = pygame.Rect(
                    col * (SEQUARE_HEIGHT + PADDING),
                    60 + row * (SEQUARE_HEIGHT + PADDING),
                    SEQUARE_HEIGHT,
                    SEQUARE_WIDTH
                )
                pygame.draw.rect(win, GREEN, rect)
                # Draw small circles on valid moves
                if [row, col] in validMoves and isWinner == False:
                    pygame.draw.circle(
                        win, GREY, (rect.centerx, rect.centery), 10)

        # Draw disks
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] is not None:
                    self.board[row][col].drawDisk(win)

        if isWinner:
            text = ""

            if blacks > whites:
                text = "Black won!"
            elif blacks == whites:
                text = "Tie!"
            else:
                text = "White Won!"

            textFont = pygame.font.Font(None, 70)
            winner_text = textFont.render(
                f"{text}", True, RED)
            winner_text_rect = winner_text.get_rect(
                midbottom=(WIDTH // 2, (HEIGHT + 60) // 2))
            win.blit(winner_text, winner_text_rect)

        pygame.display.update()

    def putDisk(self, row, col, disk):
        if self.board[row][col] != None:
            return False
        else:
            self.board[row][col] = disk
            return True

    def getNumberOfDisks(self):
        blacks = 0
        whites = 0
        for i in range(ROWS):
            for j in range(COLS):
                if self.board[i][j] == None:
                    continue
                if self.board[i][j].checkColor(BLACK):
                    blacks += 1
                if self.board[i][j].checkColor(WHITE):
                    whites += 1

        return blacks, whites

    def evaluateState(self):
        blacks, whites = self.getNumberOfDisks()
        return whites - blacks

    def findWinner(self):

        if self.player == 0:
            return True
        if self.computer == 0:
            return True

        playerValidMoves = self.getAllValidMoves(BLACK)
        computerValidMoves = self.getAllValidMoves(WHITE)

        if playerValidMoves == [] and computerValidMoves == []:
            return True

        return False

    def checkValidMove(self, row, col, color):

        outFlanked = self.getOutFlankedDisks(row, col, color)
        if len(outFlanked) == 0:
            return False
        else:
            return True

    def getAllValidMoves(self, color):
        moves = []
        for i in range(ROWS):
            for j in range(COLS):
                if self.checkValidMove(i, j, color):
                    moves.append((i, j))
        return moves

    def printAllValidMoves(self, color):
        moves = []
        for i in range(ROWS):
            for j in range(COLS):
                if self.checkValidMove(i, j, color):
                    moves.append((i, j))
        return moves

    def getOutFlankedDisks(self, row, col, color):
        oppositeColor = color
        if color == BLACK:
            oppositeColor = WHITE
        else:
            oppositeColor = BLACK

        outFlankedList = []
        if row < 0 or row >= ROWS or col < 0 or col >= COLS:
            return outFlankedList

        if self.board[row][col] is not None:
            return outFlankedList

        # Check horizontally
        newList = []
        for tempCol in range(col + 1, COLS):
            newList.append(self.board[row][tempCol])
            if self.board[row][tempCol] is None:
                break

            elif not self.board[row][col + 1].checkColor(oppositeColor):
                break

            elif self.board[row][tempCol].checkColor(oppositeColor):
                continue
            elif not self.board[row][tempCol].checkColor(oppositeColor):
                outFlankedList.extend(newList)
                break

        newList = []
        for tempCol in range(col - 1, -1, -1):

            newList.append(self.board[row][tempCol])

            if self.board[row][tempCol] is None:
                break
            elif not self.board[row][col - 1].checkColor(oppositeColor):
                break

            elif self.board[row][tempCol].checkColor(oppositeColor):
                continue
            elif not self.board[row][tempCol].checkColor(oppositeColor):
                outFlankedList.extend(newList)
                break

        # Check vertically
        newList = []
        for tempRow in range(row + 1, ROWS):

            newList.append(self.board[tempRow][col])

            if self.board[tempRow][col] is None:
                break
            elif not self.board[row+1][col].checkColor(oppositeColor):
                break
            elif self.board[tempRow][col].checkColor(oppositeColor):
                continue
            elif not self.board[tempRow][col].checkColor(oppositeColor):
                outFlankedList.extend(newList)
                break

        newList = []
        for tempRow in range(row - 1, -1, -1):
            newList.append(self.board[tempRow][col])
            if self.board[tempRow][col] is None:
                break
            elif not self.board[row - 1][col].checkColor(oppositeColor):
                break
            elif self.board[tempRow][col].checkColor(oppositeColor):
                continue
            elif not self.board[tempRow][col].checkColor(oppositeColor):
                outFlankedList.extend(newList)
                break

        return outFlankedList

    def outFlank(self, outFlankedList, color):
        for disk in outFlankedList:
            disk.setColor(color)

    def makeMove(self, row, col, color):
        outflankedList = self.getOutFlankedDisks(row, col, color)
        self.outFlank(outflankedList, color)
        if len(outflankedList) != 0:
            if color == BLACK:
                self.player -= 1
            else:
                self.computer -= 1
            # Corrected the order of row and col
            disk = Disk(row, col, color)
            disk.getCordinates()  # Update the disk's coordinates
            self.putDisk(row, col, disk)
            return True

        else:
            print("Invalid Move")
            return False
