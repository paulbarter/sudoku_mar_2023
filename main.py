import sys

board = ['-', '-', '-', '2', '6', '-', '7', '-', '1',
         '6', '8', '-', '-', '7', '-', '-', '9', '-',
         '1', '9', '-', '-', '-', '4', '5', '-', '-',
         '8', '2', '-', '1', '-', '-', '-', '4', '-',
         '-', '-', '4', '6', '-', '2', '9', '-', '-',
         '-', '5', '-', '-', '-', '3', '-', '2', '8',
         '-', '-', '9', '3', '-', '-', '-', '7', '4',
         '-', '4', '-', '-', '5', '-', '-', '3', '6',
         '7', '-', '3', '-', '1', '8', '-', '-', '-']

filled_in_board = {
    'A1': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'A2': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'A3': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'A4': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'A5': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'A6': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'A7': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'A8': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'A9': set([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    'B1': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'B2': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'B3': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'B4': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'B5': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'B6': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'B7': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'B8': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'B9': set([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    'C1': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'C2': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'C3': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'C4': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'C5': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'C6': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'C7': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'C8': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'C9': set([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    'D1': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'D2': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'D3': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'D4': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'D5': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'D6': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'D7': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'D8': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'D9': set([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    'E1': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'E2': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'E3': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'E4': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'E5': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'E6': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'E7': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'E8': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'E9': set([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    'F1': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'F2': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'F3': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'F4': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'F5': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'F6': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'F7': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'F8': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'F9': set([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    'G1': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'G2': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'G3': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'G4': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'G5': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'G6': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'G7': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'G8': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'G9': set([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    'H1': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'H2': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'H3': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'H4': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'H5': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'H6': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'H7': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'H8': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'H9': set([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    'I1': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'I2': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'I3': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'I4': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'I5': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'I6': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'I7': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'I8': set([1, 2, 3, 4, 5, 6, 7, 8, 9]), 'I9': set([1, 2, 3, 4, 5, 6, 7, 8, 9])
}

ABCDEFGHI = 'ABCDEFGHI'

def map_row_to_letter(row_num):
    return ABCDEFGHI[row_num - 1]

def get_filled_in_row(row_num):
    row = []
    for col in range(0, 9):
        row.append(filled_in_board[map_row_to_letter(row_num) + str(col + 1)])
    return row

def get_filled_in_col(col_num):
    col = []
    for row in range(0, 9):
        row_reference = ABCDEFGHI[row] + str(col_num)
        col.append(filled_in_board[row_reference])
    return col

def get_filled_in_block(block_num):
    block = []
    if block_num == 1:
        block = get_filled_in_row(1)[:3] + get_filled_in_row(2)[:3] + get_filled_in_row(3)[:3]
    elif block_num == 2:
        block = get_filled_in_row(1)[3:6] + get_filled_in_row(2)[3:6] + get_filled_in_row(3)[3:6]
    elif block_num == 3:
        block = get_filled_in_row(1)[6:9] + get_filled_in_row(2)[6:9] + get_filled_in_row(3)[6:9]
    elif block_num == 4:
        block = get_filled_in_row(4)[:3] + get_filled_in_row(5)[:3] + get_filled_in_row(6)[:3]
    elif block_num == 5:
        block = get_filled_in_row(4)[3:6] + get_filled_in_row(5)[3:6] + get_filled_in_row(6)[3:6]
    elif block_num == 6:
        block = get_filled_in_row(4)[6:9] + get_filled_in_row(5)[6:9] + get_filled_in_row(6)[6:9]
    elif block_num == 7:
        block = get_filled_in_row(7)[:3] + get_filled_in_row(8)[:3] + get_filled_in_row(9)[:3]
    elif block_num == 8:
        block = get_filled_in_row(7)[3:6] + get_filled_in_row(8)[3:6] + get_filled_in_row(9)[3:6]
    elif block_num == 9:
        block = get_filled_in_row(7)[6:9] + get_filled_in_row(8)[6:9] + get_filled_in_row(9)[6:9]
    return block

def get_element_ref(row_num, col_num):
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    cols = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return rows[row_num - 1] + cols[col_num - 1]

def initialise_board(filled_in_board, board):
    for row in range(1, 10):
        for col in range(1, 10):
            board_array_position_from_row_and_col = ((row - 1) * 9) + col - 1
            initial_board_element = board[board_array_position_from_row_and_col]
            if initial_board_element != '-':
                filled_in_board[get_element_ref(row, col)] = set([int(initial_board_element)])

def print_filled_board():
    for row in range(1, 10):
        print(get_filled_in_row(row))

def remove_selections(list_of_possibilities, actual_value):
    # received a list of matrices of possible values, and then removes the actual value
    for possibilities in list_of_possibilities:
        if len(possibilities) > 1:
            if actual_value in possibilities:
                possibilities.remove(actual_value)

def check_rows():
    for row in range(1, 10):
        row_elements = get_filled_in_row(row)
        for elements in row_elements:
            if len(elements) == 1:
                remove_selections(row_elements, sorted(elements)[0])
                continue

def check_cols():
    for col in range(1, 10):
        col_elements = get_filled_in_col(col)
        for elements in col_elements:
            if len(elements) == 1:
                remove_selections(col_elements, sorted(elements)[0])
                continue

def check_blocks():
    for block in range(1, 10):
        block_elements = get_filled_in_block(block)
        for elements in block_elements:
            if len(elements) == 1:
                remove_selections(block_elements, sorted(elements)[0])
                continue

def check_win():
    for possibilities in filled_in_board.items():
        if len(possibilities[1]) > 1:
            return False
    return True

def main(args):
    # print('arg1: {} arg2: {}'.format(args[0], args[1]))
    initialise_board(filled_in_board, board)
    win = False
    while not win:
        check_rows()
        check_cols()
        check_blocks()
        win = check_win()

    print_filled_board()

if __name__ == '__main__':
    main(sys.argv)