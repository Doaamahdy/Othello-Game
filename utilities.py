import math
import copy


ROWS, COLS = 8, 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 120, 0)

def alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.findWinner():
        return board.evaluateState()
    if maximizing_player:
        value = -math.inf
        for  newBoard in getAllValidMoves(board,WHITE): 
            value = max(value, alpha_beta(newBoard[0], depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Beta cut-off
        return value
    else:
        value = math.inf
        for newBoard in getAllValidMoves(board,BLACK):
            value = min(value, alpha_beta(newBoard[0], depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cut-off
        return value
    
    
#children
def getAllValidMoves(board,color):
    boards = []
    for i in range(ROWS):
        for j in range(COLS):                
            if board.checkValidMove(i,j,color):
                newBoard = copy.deepcopy(board)
                newBoard.makeMove(i, j,color)
                boards.append([newBoard, [i,j]])
       
    return boards     

def getBestMove(board,level):
    bestMove = -math.inf
    depth = level
    x = -1 
    y = -1

    for newBoard in getAllValidMoves(board,WHITE):
        value = alpha_beta(newBoard[0], depth,  -math.inf, math.inf, True)
        if value >= bestMove: 
            bestMove = value
            x,y = newBoard[1]  
    return x,y
