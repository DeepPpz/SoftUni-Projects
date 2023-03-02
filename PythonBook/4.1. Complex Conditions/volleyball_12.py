import math

year = input().lower()
holidays = int(input())
home = int(input())

holidays *= 2 / 3
days = (48 - home) * 3 / 4
days += holidays + home

if year == 'leap':
    days *= 1.15

print(f'{math.floor(days)}')