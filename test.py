from functions import *


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


boards = init_board()
boards[0][0] = boards[0][1] = boards[0][2] = 'X'
    # boards[1][0] = boards[1][1] = boards[1][2] =\
    # boards[2][0] = boards[2][1] = boards[2][2] = \
    # boards[0][0] = boards[1][0] = boards[1][0] = \
    # boards[0][1] = boards[1][1] = boards[2][1] = \
    # boards[0][2] = boards[1][2] = boards[2][2] = \
    # boards[0][0] = boards[1][1] = boards[2][2] = \
    # boards[2][0] = boards[1][1] = boards[0][2] = 'X'
print_board(boards)


    # elif has_won('X') or has_won('0'):
    #     turns = False
    #     pass
    # elif has_won('0'):
    #     turns = False
    #     pass
    else:
        print_board(boards)
        get_move('Player1')
        print_board(boards)
        get_move('Player2')


print_board(boards)

