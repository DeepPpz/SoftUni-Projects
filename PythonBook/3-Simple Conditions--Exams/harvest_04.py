import math

area = int(input())
grapes = float(input())
order = int(input())
workers = int(input())

area *= 0.40
grapes *= area
total_wine = grapes / 2.50
diff = abs(total_wine - order)

if order > total_wine:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(total_wine)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.ceil(diff/workers)} liters per person.")