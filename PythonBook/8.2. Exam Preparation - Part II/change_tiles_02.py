import math

budget = float(input())
width = float(input())
length = float(input())
side_brick = float(input())
height_brick = float(input())
price_brick = float(input())
price_worker = float(input())

room_area = width * length
brick_area = side_brick * height_brick / 2
total_bricks = math.ceil(room_area / brick_area) + 5
total_expenses = total_bricks * price_brick + price_worker

diff = budget - total_expenses

if diff >= 0:
    print(f"{diff:.2f} lv left.")
else:
    print(f"You'll need {abs(diff):.2f} lv more.")
