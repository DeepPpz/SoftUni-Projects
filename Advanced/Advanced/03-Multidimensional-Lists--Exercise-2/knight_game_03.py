SIZE = int(input())
chess_board = [[x for x in input()] for _ in range(SIZE)]
removed_knights = 0
possible_positions = (
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (2, 1), (2, -1),
    (1, 2), (1, -2)
)

total_knights = {}
for r in range(SIZE):
    for c in range(SIZE):
        if chess_board[r][c] == "K":
            total_knights[(r, c)] = 0

while True:
    for knight in total_knights:
        for pos in possible_positions:
            if (knight[0] + pos[0], knight[1] + pos[1]) in total_knights:
                total_knights[knight] += 1

    if all(value == 0 for value in total_knights.values()):
        break

    top_knight = next(iter(dict(sorted(total_knights.items(), key=lambda x: -x[1]))))
    chess_board[top_knight[0]][top_knight[1]] = "0"
    del total_knights[top_knight]
    removed_knights += 1

    for knight in total_knights:
        total_knights[knight] = 0

print(removed_knights)
