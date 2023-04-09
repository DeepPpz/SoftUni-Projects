n = int(input())
ships = []
total_destroyed = 0

for row in range(n):
    ships.append(list(map(int, (input().split(" ")))))

attacks = [x for x in input().split()]

for a in attacks:
    row, col = map(int, a.split("-"))

    if ships[row][col] != 0:
        ships[row][col] -= 1
        if ships[row][col] == 0:
            total_destroyed += 1

print(total_destroyed)
