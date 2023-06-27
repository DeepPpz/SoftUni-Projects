import math


def finding_closest_point(a, b):
    if a >= b:
        return True
    return False


coordinates = [math.floor(float(input())) for _ in range(8)]
sum_a = abs(coordinates[0]) + abs(coordinates[1])
sum_b = abs(coordinates[2]) + abs(coordinates[3])
sum_c = abs(coordinates[4]) + abs(coordinates[5])
sum_d = abs(coordinates[6]) + abs(coordinates[7])

if finding_closest_point(sum_a + sum_b, sum_c + sum_d):
    if sum_a <= sum_b:
        print(f'{tuple(coordinates[:2])}{tuple(coordinates[2:4])}')
    else:
        print(f'{tuple(coordinates[2:4])}{tuple(coordinates[:2])}')
else:
    if sum_c <= sum_d:
        print(f'{tuple(coordinates[4:6])}{tuple(coordinates[6:])}')
    else:
        print(f'{tuple(coordinates[6:])}{tuple(coordinates[4:6])}')
