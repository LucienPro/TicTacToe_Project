"""
Tic Tac Toe Player
"""

import math

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
    compteur_x = sum(row.count(X) for row in board);
    compteur_o = sum(row.count(O) for row in board);

    if compteur_x > compteur_o:
        return O
    else:
        return X

#Returns set of all possible actions (i, j) available on the board.
def actions(board):
    actions_possibles = set();

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_possibles.add((i,j))

    return actions_possibles;


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError

#Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
def utility(board):
    gagnant = winner(board);
    if gagnant == X:
        return 1;
    elif gagnant == 0:
        return -1;
    else:
        return 0;


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
