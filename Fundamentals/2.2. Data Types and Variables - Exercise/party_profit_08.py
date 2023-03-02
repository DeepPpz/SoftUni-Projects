import math

group_size = int(input())
days = int(input())

total_coins = 0

for d in range(1, days + 1):
    if d % 10 == 0:
        group_size -= 2
    if d % 15 == 0:
        group_size += 5

    total_coins += 50
    total_coins -= 2 * group_size

    if d % 3 == 0:
        total_coins -= 3 * group_size
    if d % 5 == 0:
        total_coins += 20 * group_size
        if d % 3 == 0:
            total_coins -= 2 * group_size

split_coins = math.floor(total_coins / group_size)

print(f'{group_size} companions received {split_coins} coins each.')