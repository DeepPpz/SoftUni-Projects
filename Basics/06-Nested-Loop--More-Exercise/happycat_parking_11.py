days_count = int(input())
hours_count = int(input())

day_sum = 0
total_sum = 0

for day in range(1, days_count + 1):
    for hour in range(1, hours_count + 1):
        if day % 2 == 0 and not hour % 2 == 0:
            day_sum += 2.50
        elif not day % 2 == 0 and hour % 2 == 0:
            day_sum += 1.25
        else:
            day_sum += 1.00

    print(f'Day: {day} - {day_sum:.2f} leva')
    total_sum += day_sum
    day_sum = 0

print(f'Total: {total_sum:.2f} leva')