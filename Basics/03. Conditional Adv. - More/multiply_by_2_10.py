num = float(input())

while True:
    if num <0:
        print('Negative number!')
        break

    num = num * 2
    print(f'Result: {num:.2f}')
    num = float(input())