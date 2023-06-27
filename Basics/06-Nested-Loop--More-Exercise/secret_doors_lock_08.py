limit_first = int(input())
limit_second = int(input())
limit_third = int(input())

for a in range(1, limit_first + 1):
    if a % 2 != 0:
        continue
    for b in range(1, limit_second + 1):
        if b not in [2, 3, 5, 7]:
            continue
        for c in range(1, limit_third + 1):
            if c % 2 == 0:
                print(f'{a} {b} {c}')
