quantity = int(input())
days_left = int(input())

total_cost, total_spirit = 0, 0

for day in range(1, days_left +1):
    if day % 11 == 0:
        quantity += 2
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += 5 + 3 + 15
    if day % 5 == 0:
        total_cost += 15 * quantity
        total_spirit += 17
    if day % 3 == 0:
        total_cost += (5 + 3) * quantity
        total_spirit += 3 + 10
    if day % 2 == 0:
        total_cost += 2 * quantity
        total_spirit += 5
    if day % 5 == 0 and day % 3 == 0:
        total_spirit += 30

if days_left % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')