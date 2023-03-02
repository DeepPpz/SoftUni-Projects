age = float(input())
gender = input()

if age < 16:
    if gender == 'f':
        print('Miss')
    elif gender == 'm':
        print('Master')
else:
    if gender == 'f':
        print('Ms.')
    elif gender == 'm':
        print('Mr.')