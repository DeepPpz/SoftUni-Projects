def find_multiplication_sign(l):
    counter, zero = 0, False
    for el in l:
        if el < 0:
            counter += 1
        elif el == 0:
            zero = True
            break
    if zero:
        print('zero')
    elif counter % 2 == 0:
        print('positive')
    else:
        print('negative')


numbers = [int(input()) for x in range(3)]
find_multiplication_sign(numbers)