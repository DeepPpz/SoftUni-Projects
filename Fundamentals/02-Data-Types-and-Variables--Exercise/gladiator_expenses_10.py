loses = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

counter = 0
expenses = 0

for lose in range(1, loses + 1):
    if lose % 2 == 0:
        expenses += helmet
    if lose % 3 == 0:
        expenses += sword
        if lose % 2 == 0:
            expenses += shield
            counter += 1

    if counter == 2:
        expenses += armor
        counter = 0

print(f'Gladiator expenses: {expenses:.2f} aureus')
