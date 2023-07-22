n = int(input())

for a in range(1, 10):
    if n % a == 0:
        for b in range(1, 10):
            if n % b == 0:
                for c in range(1, 10):
                    if n % c == 0:
                        for d in range(1, 10):
                            if n % d == 0:
                                print(f"{a}{b}{c}{d}", end=' ')
