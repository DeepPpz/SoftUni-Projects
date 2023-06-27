start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combinations = 0
comb_flag = False

for x1 in range(start_interval, end_interval + 1):
    for x2 in range(start_interval, end_interval + 1):
        combinations += 1
        if x1 + x2 == magic_number:
            comb_flag = True
            break
        else:
            continue
    if comb_flag:
        break

if comb_flag:
    print(f'Combination N:{combinations} ({x1} + {x2} = {magic_number})')
else:
    print(f'{combinations} combinations - neither equals {magic_number}')
