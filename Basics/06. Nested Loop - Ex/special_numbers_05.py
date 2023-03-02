num = int(input())

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if num % a == 0 and num % b == 0 and num % c == 0 and num % d == 0:
                    print(f'{a}{b}{c}{d}', end= ' ')