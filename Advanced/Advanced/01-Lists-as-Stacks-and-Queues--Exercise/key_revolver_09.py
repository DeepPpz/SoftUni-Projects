from collections import deque

price_bullet = int(input())
barrel_size = int(input())
all_bullets = deque(int(x) for x in input().split())
all_locks = deque(int(x) for x in input().split())
intelligence_value = int(input())
money_spend = 0
barrel = barrel_size

while all_bullets and all_locks:
    bullet = all_bullets.pop()
    lock = all_locks.popleft()

    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        all_locks.appendleft(lock)

    money_spend += price_bullet
    barrel -= 1

    if barrel == 0 and all_bullets:
        print("Reloading!")
        barrel = barrel_size

if all_locks:
    print(f"Couldn't get through. Locks left: {len(all_locks)}")
else:
    print(f"{len(all_bullets)} bullets left. Earned ${intelligence_value - money_spend}")
