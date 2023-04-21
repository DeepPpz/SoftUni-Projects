magic_num = int(input())

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        curr_num = a * b * c * d * e * f
                        if curr_num == magic_num:
                            print(f"{a}{b}{c}{d}{e}{f}", end=' ')
