n = int(input())

filled = 0

for i in range(n):
    litres = int(input())

    if litres > 255 - filled:
        print('Insufficient capacity!')
    else:
        filled += litres

print(filled)