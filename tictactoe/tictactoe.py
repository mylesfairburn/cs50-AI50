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


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    xCount = sum(row.count(X) for row in board)
    oCount = sum(row.count(O) for row in board)
    return X if xCount == oCount else O  # X makes the first move


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if board[i][j] is not EMPTY:
        raise Exception("Invalid action - cell already taken.")

    newBoard = [row[:] for row in board]
    newBoard[i][j] = player(board)
    return newBoard


def winner(board):
    """
        Returns the winner of the game, if there is one.
    """
    lines = list(board)  # rows
    lines += [[board[i][j] for i in range(3)] for j in range(3)]  # columns
    lines.append([board[i][i] for i in range(3)])  # diagonal left-to-right
    lines.append([board[i][2 - i] for i in range(3)])  # diagonal right-to-left

    for a, b, c in lines:
        if a is not None and a == b == c:
            return a
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell is None:
                return False # found an empty square → not over
    return True # no empties - board full - draw


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    return 1 if win == X else -1 if win == O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # initalise variables - use infinity as first move will replce it
    alpha = -math.inf
    beta = math.inf
    # store best action found - replaced when a new best move is found
    bestAction = None

    if player(board) == X:
        bestValue = -math.inf
        for action in actions(board):
            value = minValue(result(board, action), alpha, beta)
            if value > bestValue:
                bestValue = value
                bestAction = action
            alpha = max(alpha, bestValue)
    else:
        bestValue = math.inf
        for action in actions(board):
            value = maxValue(result(board, action), alpha, beta)
            if value < bestValue:
                bestValue = value
                bestAction = action
            beta = min(beta, bestValue)

    return bestAction


def maxValue(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, minValue(result(board, action), alpha, beta))  # call oposite function to satisfy minimax tree
        if v >= beta:
            return v          # prune: minimiser above won't allow this branch - optimisation
        alpha = max(alpha, v)
    return v


def minValue(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, maxValue(result(board, action), alpha, beta))  # call oposite function to satisfy minimax tree
        if v <= alpha:
            return v          # prune: maximiser above won't allow this branch - optimisation
        beta = min(beta, v)
    return v