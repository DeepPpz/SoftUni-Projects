n = int(input())

found_flag = False

for a in range(1, 9 + 1):
    for b in range(9, a, - 1):
        for c in range(0, 9 + 1):
            for d in range(9, c, - 1):
                if a+b+c+d == a*b*c*d:
                    if n % 10 == 5:
                        print(f'{a}{b}{c}{d}')
                        found_flag = True
                        break
                elif (a*b*c*d) // (a+b+c+d) == 3:
                    if n % 3 == 0:
                        print(f'{d}{c}{b}{a}')
                        found_flag = True
                        break
            if found_flag:
                break
    if found_flag:
        break

if not found_flag:
    print('Nothing found')
