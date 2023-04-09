def valid_cell(row, col, ldiag, rdiag):
    if row < 0:
        return False
    elif col < 0:
        return False
    elif row in attacked_positions[0] or col in attacked_positions[1]:
        return False
    elif ldiag in attacked_positions[2] or rdiag in attacked_positions[3]:
        return False
    return True


def set_queen(row, col, ldiag, rdiag):
    chessboard[row][col] = "*"
    attacked_positions[0].add(row)
    attacked_positions[1].add(col)
    attacked_positions[2].add(ldiag)
    attacked_positions[3].add(rdiag)


def remove_queen(row, col, ldiag, rdiag):
    chessboard[row][col] = "-"
    attacked_positions[0].remove(row)
    attacked_positions[1].remove(col)
    attacked_positions[2].remove(ldiag)
    attacked_positions[3].remove(rdiag)


def find_positions(row, chessboard, attacked_positions):
    if row == 8:
        for r in chessboard:
            print(*r, sep=' ', end='\n')
        print()
        return

    for col in range(8):
        ldiag = col - row
        rdiag = col + row
        if valid_cell(row, col, ldiag, rdiag):
            set_queen(row, col, ldiag, rdiag)
            find_positions(row + 1, chessboard, attacked_positions)
            remove_queen(row, col, ldiag, rdiag)


chessboard = []
attacked_positions = [set(), set(), set(), set()]

for _ in range(8):
    chessboard.append(["-" for _ in range(8)])

find_positions(0, chessboard, attacked_positions)
