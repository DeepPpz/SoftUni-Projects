m = int(input())

print_counter = 0
password = 0
pass_key = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and (a * b) + (c * d) == m:
                    print(f'{a}{b}{c}{d}', end= ' ')
                    print_counter += 1

                    if print_counter == 4:
                        password = f'{a}{b}{c}{d}'
                        pass_key = True

print()
if pass_key:
    print(f'Password: {password}')
else:
    print('No!')