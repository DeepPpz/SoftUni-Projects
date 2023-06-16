size = 8
chess_board = [[x for x in input().split()] for _ in range(size)]
end, winner, square = '', '', ''
all_moves = {
    'white_up': (-1, 0),
    'white_left': (-1, -1),
    'white_right': (-1, 1),
    'black_down': (1, 0),
    'black_left': (1, -1),
    'black_right': (1, 1)
}

white = tuple()
black = tuple()
for row in range(size):
    if 'w' in chess_board[row]:
        white = (row, chess_board[row].index('w'))
    if 'b' in chess_board[row]:
        black = (row, chess_board[row].index('b'))

while True:
    # white logic
    left_diag = (white[0] + all_moves['white_left'][0], white[1] + all_moves['white_left'][1])
    right_diag = (white[0] + all_moves['white_right'][0], white[1] + all_moves['white_right'][1])

    if left_diag == black:
        end = 'capture'
        winner = 'White'
        square = f'{chr(97 + left_diag[1])}' + f'{8 - left_diag[0]}'
        break
    elif right_diag == black:
        end = 'capture'
        winner = 'White'
        square = f'{chr(97 + right_diag[1])}' + f'{8 - right_diag[0]}'
        break

    white = (white[0] + all_moves['white_up'][0], white[1] + all_moves['white_up'][1])

    if white[0] == 0:
        end = 'promote'
        winner = 'White'
        square = f'{chr(97 + white[1])}' + f'{8 - white[0]}'
        break

    # black logic
    left_diag = (black[0] + all_moves['black_left'][0], black[1] + all_moves['black_left'][1])
    right_diag = (black[0] + all_moves['black_right'][0], black[1] + all_moves['black_right'][1])

    if left_diag == white:
        end = 'capture'
        winner = 'Black'
        square = f'{chr(97 + left_diag[1])}' + f'{8 - left_diag[0]}'
        break
    elif right_diag == white:
        end = 'capture'
        winner = 'Black'
        square = f'{chr(97 + right_diag[1])}' + f'{8 - right_diag[0]}'
        break

    black = (black[0] + all_moves['black_down'][0], black[1] + all_moves['black_down'][1])

    if black[0] == 7:
        end = 'promote'
        winner = 'Black'
        square = f'{chr(97 + black[1])}' + f'{8 - black[0]}'
        break

if end == 'capture':
    print(f'Game over! {winner} win, capture on {square}.')
elif end == 'promote':
    print(f'Game over! {winner} pawn is promoted to a queen at {square}.')
