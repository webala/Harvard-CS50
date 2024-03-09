"""
Tic Tac Toe Player
"""

import math, copy

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
    X makes the first move
    That means that if the number of X and Y on the board are equal then it is X turn
    """
    x_count = sum([arr.count(X) for arr in board])
    o_count = sum([arr.count(O) for arr in board])
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    Use a double loop to find the cells with an empty state.
    If the cell is empty add the (row, cell) indexes to the available actions
    """
    available_actions = []
    for row in range(0, len(board)):
        for cell in range(0, len(row)):
            if cell == EMPTY:
                action = (row, cell)
                available_actions.append(action)

    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, cell = action
    # The indexes cant be greater thean 2
    if row > 2 or cell > 2:
        raise Exception("Invalid action")
    
    # The action can't lead to a slot that has already been played
    # The slot should be empty
    if board[row][cell] != EMPTY:
        raise Exception("Can't move to that slot")
    
    # Do a deep copy of the board
    final_board = copy.deepcopy(board)
    # Determine whose turn it is using the player function
    player = player(board)
    # set the state of the final board with row and cell from action
    final_board[row][cell] = player

    return final_board
    
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    
    # Check the columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 'X'
            elif board[0][col] == 'O':
                return 'O'
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == 'X':
            return 'X'
        elif board[1][1] == 'O':
            return 'O'
    
    # No winner, check for tie
    if all(all(cell != EMPTY for cell in row) for row in board):
        return None  # Tie
    else:
        return None  # Game in progress
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
