import sys
n = int(input())

odd_sum, even_sum = 0, 0
odd_min, even_min = sys.maxsize, sys.maxsize
odd_max, even_max = - sys.maxsize, - sys.maxsize
odd_flag, even_flag = True, True

for i in range(1, n + 1):
    num = float(input())

    if i % 2 == 0:
        even_flag = False
        even_sum += num
        if even_max < num: even_max = num
        if even_min > num: even_min = num
    else:
        odd_flag = False
        odd_sum += num
        if odd_max < num: odd_max = num
        if odd_min > num: odd_min = num

print(f'OddSum={odd_sum},')
if odd_flag:
    print('OddMin=No,')
    print('OddMax=No,')
else:
    print(f'OddMin={odd_min},')
    print(f'OddMax={odd_max},')
print(f'EvenSum={even_sum},')
if even_flag:
    print('EvenMin=No,')
    print('EvenMax=No')
else:
    print(f'EvenMin={even_min},')
    print(f'EvenMax={even_max:}')