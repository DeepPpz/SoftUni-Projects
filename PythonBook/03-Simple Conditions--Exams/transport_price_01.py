distance = int(input())
part_day = input()

total_price = 0

if part_day == 'day':
    taxi_rate = 0.79
elif part_day == 'night':
    taxi_rate = 0.90

if distance >= 100:
    total_price = distance * 0.06
elif distance >= 20:
    total_price = distance * 0.09
else:
    total_price = 0.70 + distance * taxi_rate

print(total_price)