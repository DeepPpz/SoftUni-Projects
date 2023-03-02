projection = input()
rows = int(input())
columns = int(input())

capacity = rows * columns
total_income = 0

if projection == 'Premiere':
    total_income = capacity * 12
elif projection == 'Normal':
    total_income = capacity * 7.50
elif projection == 'Discount':
    total_income = capacity * 5

print(f'{total_income:.2f} leva')