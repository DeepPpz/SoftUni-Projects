prev_year = int(input())

range_list = range(0, 10)


def new_year():
    for a in range_list:
        for b in range_list:
            if b != a:
                for c in range_list:
                    if c not in [a, b]:
                        for d in range_list:
                            if d not in [a, b, c] and int(f'{a}{b}{c}{d}') > prev_year:
                                print(f'{a}{b}{c}{d}')
                                return


new_year()