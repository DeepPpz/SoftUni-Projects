number = float(input())

in_range = (100 <= number <= 200) or number == 0

if not in_range:
    print('invalid')