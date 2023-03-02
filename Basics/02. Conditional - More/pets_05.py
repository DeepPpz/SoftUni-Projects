days = int(input())
left_food = int(input())
dog_needs = float(input())
cat_needs = float(input())
turtle_needs = float(input())

total_food = dog_needs * days
total_food += cat_needs * days
total_food += turtle_needs / 1000 * days

import math

if left_food >= total_food:
    print(f'{math.floor(left_food - total_food)} kilos of food left.')
else:
    print(f'{math.ceil(total_food - left_food)} more kilos of food are needed.')