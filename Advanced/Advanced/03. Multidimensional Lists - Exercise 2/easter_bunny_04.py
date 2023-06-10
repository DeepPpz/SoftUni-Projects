def in_range(row, col):
    return 0 <= row < SIZE and 0 <= col < SIZE


def collect_eggs(row, col, eggs, steps):
    if not in_range(row, col) or field[row][col] == 'X':
        results[direction].append(eggs)
        results[direction].append(steps)
    else:
        steps.append([row, col])
        eggs += int(field[row][col])
        collect_eggs(row + r, col + c, eggs, steps)


SIZE = int(input())
field = [[x for x in input().split()] for _ in range(SIZE)]
results = {}
all_directions = {
    "right": (0, 1),
    "left": (0, -1),
    "down": (1, 0),
    "up": (-1, 0)
}

bunny = tuple()
for row in range(SIZE):
    if "B" in field[row]:
        bunny = (row, field[row].index("B"))
        break

for (direction, change) in all_directions.items():
    results[direction] = []
    r, c = change[0], change[1]

    collect_eggs(bunny[0] + r, bunny[1] + c, 0, [])

best_result = next(iter(sorted(results.items(), key=lambda x: -x[1][0])))
print(best_result[0])
print(*best_result[1][1], sep='\n')
print(best_result[1][0])
