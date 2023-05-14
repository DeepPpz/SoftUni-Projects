from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))
completed = True

for order in orders.copy():
    if order <= food_quantity:
        food_quantity -= orders.popleft()
    else:
        completed = False
        break

if completed:
    print("Orders complete")
else:
    print("Orders left: ", end='')
    print(* orders, sep=' ')
