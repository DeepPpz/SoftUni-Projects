from collections import deque

kids = deque([x for x in input().split()])
potato_toss = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-potato_toss)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.pop()}")
