import os
import sys
import time
import random


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


def init_board(board_size: int = 3, empty_field: str = '.') -> list:
    """ function to return board in size of board_size nested, with empty field

    :param empty_field: (str) def '.'
    :param board_size: (int) size of elements in the same number of nested lists
    :return: board - board size number of nested lists with board size of elements
    """

    board = []  # TO DO list comprehension
    for list_lvl0 in range(board_size):
        board.append([])
        for list_lvl1 in range(board_size):
            board[list_lvl0].append(empty_field)
    return board


# 2. Implement `get_move()` that asks for user input and returns the coordinates of a valid move on board.
#     - The player specifies coordinates as letter and number: `A2` is first row and second column,
#     `C1` is third row and
#       first column, etc.
#     - The function returns a tuple of two integers: (row, col)
# ??    - The returned coordinates start from 0
#     - The integers indicate a valid (emptyemplty_field) position on the board

#     - If the user provides coordinates that are outside of board, keep asking
#     - If the user provides coordinates for a place that is taken, keep asking
#     - If the user provides input that doesn't look like coordinates, keep asking
# 9. [OPTIONAL] Allow players to quit the game anytime by typing `quit`.
#     - When the player types `quit` instead of coordinates, the program exits.
# get_move fun added


def quit_game(exit_message: str = 'Bye Bye', delay: float = 1) -> None:
    """ function to exit app when called with custom message, after delayed time

    :param exit_message: (str) custom message to print when before exit, def 'Bye Bye'
    :param delay: (float) time seconds to delay exit
    """
    print(exit_message)
    time.sleep(delay)
    sys.exit()


def available_moves(boards: list, empty_cell: str = '.') -> list:
    """function to return list of the available cells - one marks with empty_cell (str)
    on boards(nestedlist)

    :param empty_cell: (str) represents empty cell in boards)
    :param boards: list nested list of cells that is board for a game
    :return: list of available moves
    """
    available_moves_list = []
    for i_list in range(len(boards)):  # TO DO list comprehension
        for i_element in range(len(boards[i_list])):
            if boards[i_list][i_element] == empty_cell:
                available_moves_list.append((i_list, i_element))
    return available_moves_list


def translate_input_moves(inp_str: str) -> tuple:
    """returns tuple of 2 numbers from a string, its a translation of
    coordinates input by user in form a1 b2 c3 etc...

    :param inp_str: user input of coordinates
    :return: tuple of two ints which are coordinates
    """
    # correct_inp_str_list = ['a', 'b', 'c']
    if (tuple(inp_str)[0]) == 'a':
        return tuple((0, (int((tuple(inp_str)[1]))) - 1))

    if (tuple(inp_str)[0]) == 'b':
        return tuple((1, (int((tuple(inp_str)[1]))) - 1))

    if (tuple(inp_str)[0]) == 'c':
        return tuple((2, (int((tuple(inp_str)[1]))) - 1))
    # if (tuple(inp_str)[0]) not in correct_inp_str_list and (int((tuple(inp_str)[1]))) not in range(4):
    # #    return None         # call error! this is where incorrect input is coming from


def raw_available_moves(boards: list) -> list:
    raw_moves = []
    for tuples in available_moves(boards):
        raw_moves.append(list(tuples))

    for el in range(len(raw_moves)):
        if raw_moves[el][0] == 0:
            raw_moves[el][0] = 'A'
        elif raw_moves[el][0] == 1:
            raw_moves[el][0] = 'B'
        else:
            raw_moves[el][0] = 'C'
    return raw_moves


def get_move(boards: list) -> tuple:
    """function returns tuple with coordinates (row, column) from user input."""

    incorrect_input = True
    correct_move = [['a', 'b', 'c'], ['1', '2', '3']]
    while incorrect_input:
        move = input("Choose field by providing coordinates f.e.: A2:").casefold()

        if move == 'Quit'.casefold():
            quit_game()
        elif move[0] not in correct_move[0] or move[1] not in correct_move[1] or len(move) != 2 or \
                translate_input_moves(move) not in available_moves(boards):
            print(f'Wrong Input. Available moves:{raw_available_moves(boards)}')
        else:
            return translate_input_moves(move)


def get_move_ai(boards: list) -> tuple:  # not real AI computer just pick random
    time.sleep(1)
    best_score = -1000
    best_move = 0
    """function to randomly pick and return in form of tuple a move from available moves"
    :param boards: list of boards
    :return: tuple of coordinates
    """

    if len(available_moves(boards)) == 9:
        best_move = random.choice(available_moves(boards))
    else:
        for possible_move in available_moves(boards):
            mark('X', boards, possible_move[0], possible_move[1])
            score = minimax(boards, False)
            mark('.', boards, possible_move[0], possible_move[1])
            if score > best_score:
                best_score = score
                best_move = possible_move
                time.sleep(0.8)
    return best_move


def minimax(boards: list, depth: int = 0, is_maximizing: bool = False) -> tuple or list:
    # max_player = 'X' # letter
    # other_player = '0' if max_player == 'X' else 'X'

    if has_won('0', boards):
        return -100
    elif has_won('X', boards):
        return 100
    elif is_full(boards):
        return 0

    if is_maximizing:
        max_eval = -1000
        for possible_move in available_moves(boards):
            mark('X', boards, possible_move[0], possible_move[1])
            sim_eval = minimax(boards, 3, False)
            max_eval = max(max_eval, sim_eval)
            mark('.', boards, possible_move[0], possible_move[1])
        return max_eval
    else:
        min_eval = 1000
        for possible_move in available_moves(boards):
            mark('0', boards, possible_move[0], possible_move[1])
            sim_eval = minimax(boards, 3, True)
            min_eval = min(min_eval, sim_eval)
            mark('.', boards, possible_move[0], possible_move[1])
        return min_eval


def get_move_comp(boards: list) -> tuple:
    """function to randomly pick and return in form of tuple a move from available moves"

    :param boards: list of boards
    :return: tuple of coordinates
    """

    random_move: tuple = random.choice(available_moves(boards))
    time.sleep(0.8)
    return random_move


def mark(player: int or str, boards: list, row: int, col: int) -> None:
    """function to mark player move on boards

    :type boards: list
    :param player: int 1 or 2
    :param boards: list of boards where to make a mark
    :param row: int index of list in boards
    :param col: int index of element in boards
    """
    if player == 0 or player == 'X':
        player_mark = 'X'
    elif player == 1 or player == '0':
        player_mark = '0'
    else:
        player_mark = '.'

    boards[row][col] = player_mark


def has_won(player: str, boards: list) -> bool:  # TO DO pythonic
    """function to return True for if win condition is reached

    :param player: str 'X' or '0'
    :param boards: list of boards of the game
    :return: True if player has correct cells crossed
    """
    if boards[0][0] == boards[0][1] == boards[0][2] == player or \
            boards[1][0] == boards[1][1] == boards[1][2] == player or \
            boards[2][0] == boards[2][1] == boards[2][2] == player or \
            boards[0][0] == boards[1][0] == boards[2][0] == player or \
            boards[0][1] == boards[1][1] == boards[2][1] == player or \
            boards[0][2] == boards[1][2] == boards[2][2] == player or \
            boards[0][0] == boards[1][1] == boards[2][2] == player or \
            boards[2][0] == boards[1][1] == boards[0][2] == player:
        return True


def is_full(lists: list, empty_cell: str = '.') -> bool:
    """function return false if boards have still available moves

    :param empty_cell: str def '.' how the empty_cell are marked
    :param lists:
    :return:
    """
    if any(empty_cell in nested_list for nested_list in lists):
        return False
    else:
        return True


def game_over(boards: list) -> bool:
    if has_won('X', boards) or has_won('0', boards) or is_full(boards):
        return True


def print_board(boards: list) -> None:
    """function to print on-screen boards of game

    :param boards: lists of game cells
    """

    print()
    print(f'\t1   2   3\nA\t', end='')
    print(*boards[0], sep=' | ')
    print(f'\t---+---+---\nB\t', end='')
    print(*boards[1], sep=' | ')
    print(f'\t---+---+---\nC\t', end='')
    print(*boards[2], sep=' | ')
    print()


def print_result(boards: list) -> None:
    """function to print winner or draw on-screen

    :param boards: lists of boards
    """

    if has_won('X', boards) is True:
        print('X has won!')
    elif has_won('0', boards) is True:
        print('0 has won!')
    else:
        print("It's a tie!")


def tictactoe_game(mode: str = 'Players') -> None:
    """function to call the game in mode:str

    :param mode: str 'Players', 'Human-Ai', 'Ai-Human', 'Ai-Ai'
    """
    os.system('clear')
    boards = init_board()
    turns = True
    players = [0, 1]
    modes = {'HUMAN-AI': [get_move, get_move_ai],
             'AI-HUMAN': [get_move_ai, get_move],
             'AI-AI': [get_move_ai, get_move_ai],
             'Players': [get_move, get_move],
             }
    moves_list = modes.get(mode)

    while turns:
        for player in players:
            os.system('clear')
            print_board(boards)
            row, col = moves_list[player](boards)
            mark(player, boards, row, col)
            if is_full(boards) or has_won('X', boards) or has_won('0', boards):
                turns = False  # while true, break - lamie obie lupy?
                print_board(boards)
                print_result(boards)  # print_result goes again through has_won function to check = not efficient
                break


def main_manu():
    """fun to generate menu and handle menu choices"""

    while True:
        menu_choice = input("""
\t::::Tic<>Tac<>Toe::::
\t:::::::::::::::::::::
\t1. Player vs Player
\t2. Player vs Computer
        """)
        if menu_choice == 'Quit'.casefold():
            quit_game()
        elif menu_choice == '1':
            tictactoe_game()
        elif menu_choice == '2':
            menu_choice2 = input("""
            1. Player vs AI
            2. AI vs Player
            3. AI vs AI
            """)
            if menu_choice2 == '1':
                tictactoe_game('HUMAN-AI')
            elif menu_choice2 == '2':
                tictactoe_game('AI-HUMAN')
            elif menu_choice2 == '3':
                tictactoe_game('AI-AI')
            else:
                pass
        elif menu_choice == 'Quit'.casefold():
            quit_game()
        else:
            pass

