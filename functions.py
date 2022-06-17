import sys

# 1. Implement `init_board()` to return an empty 3-by-3 board, i.e.
# a list of lists filled with dots. The inner lists are
#    rows.
#     - A list of lists is returned, representing a list of rows
#     - Every cell of the returned value is `.`
#     - The rows of the returned value are independent (changing one row doesn't affect the others)
#     - Printing the result of the `init_board()` function shows the following in the terminal:
#
# ```
# [['.','.','.'],['.','.','.'],['.','.','.']]
# ```


def init_board(board_size=3):
    board = []
    for list_lvl0 in range(board_size):
        board.append([])
        for list_lvl1 in range(board_size):
            board[list_lvl0].append('.')
    return board


# 2. Implement `get_move()` that asks for user input and returns the coordinates of a valid move on board.
#     - The player specifies coordinates as letter and number: `A2` is first row and second column,
#     `C1` is third row and
#       first column, etc.
#     - The function returns a tuple of two integers: (row, col)
# ??    - The returned coordinates start from 0
#     - The integers indicate a valid (empty) position on the board

#     - If the user provides coordinates that are outside of board, keep asking
#     - If the user provides coordinates for a place that is taken, keep asking
#     - If the user provides input that doesn't look like coordinates, keep asking
# 9. [OPTIONAL] Allow players to quit the game anytime by typing `quit`.
#     - When the player types `quit` instead of coordinates, the program exits.
# get_move fun added

coordinates = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']


def get_move(player):
    """function returns tuple with coordinates (row, column) from user input."""

    if player == 'Player1':
        player_mark = 'X'
    else:
        player_mark = '0'

    incorrect_input = True
    coordinates_letter = None           # local variable is not used (by PyCharm) - not understand
    if not coordinates:
        incorrect_input = False

    while incorrect_input:
        print(coordinates)      # Debugging to be removed
        move = input("Choose field by providing coordinates f.e.: A2:").casefold()
        if move == 'Quit'.casefold():
            print('Bye Bye')
            sys.exit()
        elif move in coordinates:
            if (tuple(move)[0]) == 'a':
                coordinates_letter = 0
            elif (tuple(move)[0]) == 'b':
                coordinates_letter = 1
            else:
                coordinates_letter = 2
            boards[coordinates_letter][int(tuple(move)[1]) - 1] = player_mark
            coordinates.remove(move)
            incorrect_input = False
            return tuple(move)
        else:
            pass




# ? since fun get_move required to validate the input in terms of not used spot useless to repeat...
# 3. Implement `mark()` that writes the value of `player` (`X` or `0`) into the  `row` & `col` element of `board`.
#     - If the cell at `row` and `col` is empty (contains a dot `.`), it is marked with `player`
#     - It does not do anything if the coordinates are out of bounds
#     - It does not do anything if the cell is already marked
# def mark(player):
#     x = ('a', '3')
#     coordinates = ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3')
#     coordinates_letter = None
#
#     if player == 'Player1':
#         player_mark = 'X'
#     else:
#         player_mark = '0'
#
#     if x in coordinates:
#         if (tuple(x)[0]) == 'a':
#             coordinates_letter = 0
#         elif (tuple(x)[0]) == 'b':
#             coordinates_letter = 1
#         else:
#             coordinates_letter = 2
#     if boards[coordinates_letter][int(tuple(x)[1])-1] != '.':
#         boards[coordinates_letter][int(tuple(x)[1])-1] = player_mark
#     else:
#         pass



# 4. Implement `has_won()` that returns `True` if `player` (`X` or `0`)  has three of their marks in a horizontal,
#    vertical, or diagonal row on `board`.
#     - Returns `True` if `player` has a three-in-a-row on `board`.
#     - Returns `False` if `player` doesn't have a three-in-a-row on `board`


def has_won(player):  # to be PYTHONIC
    if boards[0][0] == boards[0][1] == boards[0][2] == player or \
            boards[1][0] == boards[1][1] == boards[1][2] == player or \
            boards[2][0] == boards[2][1] == boards[2][2] == player or \
            boards[0][0] == boards[1][0] == boards[1][0] == player or \
            boards[0][1] == boards[1][1] == boards[2][1] == player or \
            boards[0][2] == boards[1][2] == boards[2][2] == player or \
            boards[0][0] == boards[1][1] == boards[2][2] == player or \
            boards[2][0] == boards[1][1] == boards[0][2] == player:
        return True
    else:
        return False


# 5. Implement `is_full()` that returns `True` if the board is full.
#     - Returns `True` if there are no empty fields on the board
#     - Returns `False` otherwise
def is_full(lists):
    if any('.' in nested_list for nested_list in lists):
        return False
    else:
        return True


# 6.DONE Implement `print_board()` that prints the board to the screen.
#     - Players are indicated with `X` and `0`, and empty fields are indicated with dots (`.`)
#     - There are coordinates displayed around the board
#     - The board is displayed in this format:
#
# ```
#    1   2   3
# A  . | . | .
#   ---+---+---
# B  . | . | .
#   ---+---+---
# C  . | . | .
# ```


def print_board(boards):
    print(f'\t1\t2\t3\nA\t', end='')
    print(*boards[0], sep=' | ')
    print(f'   ---+---+---\nB\t', end='')
    print(*boards[1], sep=' | ')
    print(f'   ---+---+---\nC\t', end='')
    print(*boards[2], sep=' | ')


# 7. Implement `print-result()` that displays the result of the game.
#     - If player `X` wins, print "X has won!"
#     - If player `0` wins, print "0 has won!"
#     - If nobody wins, print "It's a tie!"


def print_result():
    if has_won('X') is True:
        print('X has won!')
    elif has_won('0') is True:
        print('0 has won!')
    else:
        print("It's a tie!")


# 8. Use the implemented functions to write a `tictactoe_game()` function that will run a whole 2-players game.
#     - Player X starts the game
#     - Players alternate their moves (`X`, `0`, `X`, `0`...)
#     - The board is displayed before each move, and at the end of game
#     - The game ends when someone wins or the board is full
#     - The game handles bad input (wrong coordinates) without crashing


def tictactoe_game():
    boards = init_board()
    turns = True
    players = ['Player1', 'Player2']
    while turns:
        for player in players:
            print_board(boards)
            get_move(player)
            if is_full(boards) or has_won('X') or has_won('0'):
                turns = False
                print_result()  # print_result goes again through has_won function to check = not efficient
                break



# 10. Implement player-against-AI mode. The AI can drive one of the players, and the game is fully playable against the
#     computer.
#     - When `tictactoe_game()` is called with the argument `'HUMAN-AI'` then it calls `get_ai_move()` instead
#       of `get_move()` when it's Player `0` turn
#     - When `tictactoe_game()` is called with the argument `'AI-HUMAN'` then it calls `get_ai_move()` instead
#       of `get_move()` when it's Player `X` turn
#     - Function `get_ai_move()` returns a valid move (if possible) without asking for any input
#     - Function `get_ai_move()` returns `None` if board is full
#     - Function `main_menu()` is implemented as a menu for between choosing 2-player
#       mode and against-AI mode by pressing
#       1 or 2, respectively
#
# 11. [OPTIONAL] AI is capable of recognizing the opportunity to win the game with one move.
#     - Function `get_ai_move()` picks the winning move if there is one on the board
#
# 12. [OPTIONAL] AI is capable of recognizing if its enemy could win the game with the next move,
#       and (supposing there is
#     no direct winning move) moves against it.
#     - Function `get_ai_move()` (when there is no winning move in one step) picks a move
#     which prevents a certain winning
#       move for its enemy
#     - When there is a direct winning move, function `get_ai_move()` still picks that
#     - When there are multiple one-step options for the enemy, `get_ai_move()` tries to prevent one of them
#
# 13. [OPTIONAL] AI is unbeatable in all cases.
#     - There is no strategy or combination of steps that could win the game against the AI
#
# 14. [OPTIONAL] AI can play against itself
#     - When `tictactoe_game()` is called with the argument `'AI-AI'` then it calls `get_ai_move` for both players
#     - The game comes to an end without any user input
#     - Game play is easy to follow as there is a 1 seconds delay between the moves


# if __name__ == '__main__':



tictactoe_game()