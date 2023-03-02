start_interval = int(input())
end_interval = int(input())

for a in range(start_interval, end_interval + 1):
    for b in range(start_interval, end_interval + 1):
        for c in range(start_interval, end_interval + 1):
            if (b + c) % 2 != 0:
                continue
            for d in range(start_interval, end_interval + 1):
                if a > d:
                    if a % 2 == 0:
                        if d % 2 != 0:
                            print(f'{a}{b}{c}{d}', end= ' ')
                    else:
                        if d % 2 == 0:
                            print(f'{a}{b}{c}{d}', end= ' ')