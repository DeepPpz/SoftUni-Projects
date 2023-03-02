import math

biscuits_per_day = int(input())
workers = int(input())
competing_produce = int(input())

total_bisc_day = biscuits_per_day * workers
total_produce = 0

for day in range(1, 31):
    if day % 3 == 0:
        total_produce += math.floor(total_bisc_day * 0.75)
    else:
        total_produce += total_bisc_day

diff = (total_produce - competing_produce) / competing_produce * 100

print(f'You have produced {total_produce} biscuits for the past month.')
if diff > 0:
    print(f'You produce {diff:.2f} percent more biscuits.')
else:
    print(f'You produce {abs(diff):.2f} percent less biscuits.')