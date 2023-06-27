n = int(input())

for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if a + b == c + d:
                    if n % (a + b) == 0:
                        print(f'{a}{b}{c}{d}', end=' ')
