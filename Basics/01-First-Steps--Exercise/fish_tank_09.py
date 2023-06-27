length = int(input())
width = int(input())
height = int(input())
percent_area = float(input())

capacity = length * width * height
capacity_litres = capacity / 1000
amount_litres = capacity_litres * (1 - percent_area / 100)

print(amount_litres)
