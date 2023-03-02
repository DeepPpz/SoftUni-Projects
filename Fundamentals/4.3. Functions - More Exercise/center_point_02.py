def finding_closest_point(a, b):
    if a < b:
        return True
    return False


import math

coordinates = [math.floor(float(input())) for _ in range(4)]
sum_a = sum([abs(i) for i in coordinates[:2]])
sum_b = sum([abs(i) for i in coordinates[2:]])

if finding_closest_point(sum_a, sum_b):
    print(tuple(coordinates[:2]))
else:
    print(tuple(coordinates[2:]))
