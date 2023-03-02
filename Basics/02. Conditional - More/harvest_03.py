x = int(input())
y = float(input())
z = int(input())
workers = int(input())

manuf = x * 0.4
grapes_total = manuf * y
total_litres = grapes_total / 2.5

import math

if total_litres < z:
    print(f'It will be a tough winter! More {math.floor(z - total_litres)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(total_litres)} liters.')
    print(f'{math.ceil(total_litres - z)} liters left -> {math.ceil((total_litres - z) / workers)} liters per person.')