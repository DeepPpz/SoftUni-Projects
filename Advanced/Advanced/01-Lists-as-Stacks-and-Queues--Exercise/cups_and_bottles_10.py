from collections import deque

all_cups = deque(int(x) for x in input().split())
all_bottles = deque(int(x) for x in input().split())
wasted_litres = 0

while all_cups and all_bottles:
    cup = all_cups.popleft()
    bottle = all_bottles.pop()

    if cup > bottle:
        cup -= bottle
        all_cups.appendleft(cup)
    else:
        wasted_litres += bottle - cup

if all_bottles:
    print(f"Bottles: {' '.join(str(x) for x in reversed(all_bottles))}")
if all_cups:
    print(f"Cups: {' '.join(str(x) for x in all_cups)}")
print(f"Wasted litters of water: {wasted_litres}")
