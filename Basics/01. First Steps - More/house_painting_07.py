x = float(input())
y = float(input())
h = float(input())

cons_green = 3.4
cons_red = 4.3

front_wall = x * x - 1.2 * 2
back_wall = x * x
side_walls = 2 * (x * y) - 2 * (1.5 * 1.5)
roof_1 = 2 * (x * y)
roof_2 = 2 * ((x * h) / 2)
total_green = (front_wall + back_wall + side_walls) / 3.4
total_red = (roof_1 + roof_2) / 4.3

print(f'{total_green:.2f}')
print(f'{total_red:.2f}')