n = int(input())
m = int(input())

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(97, 97 + m):
            for d in range(97, 97 + m):
                for e in range(1, n + 1):
                    if e > a and e > b:
                        print(f'{a}{b}{chr(c)}{chr(d)}{e}', end=' ')
