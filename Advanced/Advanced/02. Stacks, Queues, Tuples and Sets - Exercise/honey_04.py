from collections import deque

working_bees = deque([int(x) for x in input().split()])
total_nectar = deque([int(x)for x in input().split()])
honey_making = deque([x for x in input().split()])
made_honey = 0
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

while working_bees and total_nectar:
    bee = working_bees.popleft()
    nectar = total_nectar.pop()

    if nectar < bee:
        working_bees.appendleft(bee)
    else:
        symbol = honey_making.popleft()
        made_honey += abs(operations[symbol](bee, nectar)) if nectar > 0 else 0

print(f"Total honey made: {made_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if total_nectar:
    print(f"Nectar left: {', '.join([str(x) for x in total_nectar])}")
