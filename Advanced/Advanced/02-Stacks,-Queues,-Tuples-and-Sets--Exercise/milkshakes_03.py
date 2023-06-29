from collections import deque

chocolates = deque(map(int, input().split(", ")))
cups_milk = deque(map(int, input().split(", ")))
milkshakes = 0

while (milkshakes < 5) and (chocolates and cups_milk):
    choco = chocolates.pop()
    milk = cups_milk.popleft()

    if choco <= 0 and milk <= 0:
        continue
    elif choco <= 0:
        cups_milk.appendleft(milk)
        continue
    elif milk <= 0:
        chocolates.append(choco)
        continue

    if choco == milk:
        milkshakes += 1
    else:
        cups_milk.append(milk)
        chocolates.append(choco - 5)

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print("Chocolate:", end=' ')
if chocolates:
    print(*chocolates, sep=', ')
else:
    print("empty")
print("Milk:", end=' ')
if cups_milk:
    print(*cups_milk, sep=', ')
else:
    print("empty")
