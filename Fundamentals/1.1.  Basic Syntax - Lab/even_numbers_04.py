n = int(input())

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        continue
    else:
        print(f'{num} is odd!')
        exit()

print('All numbers are even.')