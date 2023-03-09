import sys

board = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3',
         'A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6',
         'A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9',
         'D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3',
         'D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6',
         'D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9',
         'G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3',
         'G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6',
         'G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9']

filled_in_board = {
    'A1': [1], 'A2': [], 'A3': [], 'A4': [], 'A5': [], 'A6': [], 'A7': [], 'A8': [], 'A9': [],
    'B1': [2], 'B2': [], 'B3': [], 'B4': [], 'B5': [], 'B6': [], 'B7': [], 'B8': [], 'B9': [],
    'C1': [3], 'C2': [], 'C3': [], 'C4': [], 'C5': [], 'C6': [], 'C7': [], 'C8': [], 'C9': [],
    'D1': [4], 'D2': [], 'D3': [], 'D4': [], 'D5': [], 'D6': [], 'D7': [], 'D8': [], 'D9': [],
    'E1': [5], 'E2': [], 'E3': [], 'E4': [], 'E5': [], 'E6': [], 'E7': [], 'E8': [], 'E9': [],
    'F1': [6], 'F2': [], 'F3': [], 'F4': [], 'F5': [], 'F6': [], 'F7': [], 'F8': [], 'F9': [],
    'G1': [7], 'G2': [], 'G3': [], 'G4': [], 'G5': [], 'G6': [], 'G7': [], 'G8': [], 'G9': [],
    'H1': [8], 'H2': [], 'H3': [], 'H4': [], 'H5': [], 'H6': [], 'H7': [], 'H8': [], 'H9': [],
    'I1': [9], 'I2': [], 'I3': [], 'I4': [], 'I5': [], 'I6': [], 'I7': [], 'I8': [], 'I9': []
}

def get_row(row_num):
    start_count = (row_num - 1) * 9
    row = []
    for element in range(start_count, start_count + 9):
        row.append(board[element])
    return row

def map_row_to_letter(row_num):
    row_letters = 'ABCDEFGHI'
    return row_letters[row_num - 1]

def get_filled_in_row(row_num):
    row = []
    for col in range(0, 9):
        row.append(filled_in_board[map_row_to_letter(row_num) + str(col + 1)])
    return row

def get_col(col_num):
    start_count = col_num - 1
    col = []
    for element in range(0, 9):
        col.append(board[start_count])
        start_count += 9
    return col

def get_block(block_num):
    block = []
    if block_num == 1:
        block = [get_row(1)[:3], get_row(2)[:3], get_row(3)[:3]]
    elif block_num == 2:
        block = [get_row(1)[3:6], get_row(2)[3:6], get_row(3)[3:6]]
    elif block_num == 3:
        block = [get_row(1)[6:9], get_row(2)[6:9], get_row(3)[6:9]]
    elif block_num == 4:
        block = [get_row(4)[:3], get_row(5)[:3], get_row(6)[:3]]
    elif block_num == 5:
        block = [get_row(4)[3:6], get_row(5)[3:6], get_row(6)[3:6]]
    elif block_num == 6:
        block = [get_row(4)[6:9], get_row(5)[6:9], get_row(6)[6:9]]
    elif block_num == 7:
        block = [get_row(7)[:3], get_row(8)[:3], get_row(9)[:3]]
    elif block_num == 8:
        block = [get_row(7)[3:6], get_row(8)[3:6], get_row(9)[3:6]]
    elif block_num == 9:
        block = [get_row(7)[6:9], get_row(8)[6:9], get_row(9)[6:9]]
    return block

def get_element_ref(row_num, col_num):
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    cols = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return rows[row_num - 1] + cols[col_num - 1]

def initialise_board(filled_in_board, board):
    for row in range(1,9-1):
        for col in range(1, 9-1):
            board_array_position_from_row_and_col = ((row - 1) * (col - 1)) + col - 1
            filled_in_board[get_element_ref(row, col)].append(board[board_array_position_from_row_and_col])

def print_board():
    for row in range(1, 10):
        print(get_row(row))

def print_filled__board():
    for row in range(1, 10):
        print(get_filled_in_row(row))

def main(args):
    # print('arg1: {} arg2: {}'.format(args[0], args[1]))
    print_board()
    print()
    print_filled__board()
    print()
    initialise_board(filled_in_board, board)
    print_board()
    print()
    print_filled__board()
    print()

if __name__ == '__main__':
    main(sys.argv)