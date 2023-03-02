projection = input().lower()
rows = int(input())
columns = int(input())

total_income = rows * columns

if projection == 'premiere':
    total_income *= 12
elif projection == 'normal':
    total_income *= 7.50
elif projection == 'discount':
    total_income *= 5

print(f'{total_income:.2f} leva')