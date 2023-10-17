"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

#Returns player who has the next turn on a board.
def player(board):
    compteur_x = sum(row.count(X) for row in board)
    compteur_o = sum(row.count(O) for row in board)

    if compteur_x > compteur_o:
        return O
    else:
        return X

#Returns set of all possible actions (i, j) available on the board.
def actions(board):
    actions_possibles = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_possibles.add((i,j))

    return actions_possibles


def result(board, action):
   temp_board = deepcopy(board)

   if temp_board[action[0]][action[1]] != 'X' and temp_board[action[0]][action[1]] != 'O':
    temp_board[action[0]][action[1]] = player(board)
    return temp_board
   else:
    raise actionimpossibleresult

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #lignes
    for i in range(3):       
        lv_check = str(board[i][0]) + str(board[i][1]) + str(board[i][2])
        if lv_check == 'XXX' :
            return 'X'
        elif lv_check == 'OOO':
            return 'O'
    #colonnes
    for i in range(3):       
        lv_check = str(board[0][i]) + str(board[1][i]) + str(board[2][i])
        if lv_check == 'XXX' :
            return 'X'
        elif lv_check == 'OOO':
            return 'O'  
    #1ère DIAG
    lv_check = str(board[0][0]) + str(board[1][1]) + str(board[2][2])
    if lv_check == 'XXX' :
        return 'X'
    elif lv_check == 'OOO':
        return 'O'  
    #2nd DIAG
    lv_check = str(board[0][2]) + str(board[1][1]) + str(board[2][0])
    if lv_check == 'XXX' :
        return 'X'
    elif lv_check == 'OOO':
        return 'O'
    #Sinon pas de gagnant
    return None

def terminal(board):
    # Cas True (match null ou X a gagné ou O a gagné
    if (all(all(cell != EMPTY for cell in row) for row in board)) or winner(board) == 'X' or winner(board) == 'O':
        return True

    # Jeu encore en cours Cas False
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    lv_winner = winner(board)
    if lv_winner == 'X':
        return 1
    elif lv_winner == 'O':
        return -1
    else:
        return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
