import math

needed_hours = int(input())
days_available = int(input())
workers = int(input())

hours_available = days_available * 8 * workers + 2 * days_available * workers
hours_available *= 0.90
diff = abs(hours_available - needed_hours)

if hours_available >= needed_hours:
    print(f'Yes!{math.floor(diff)} hours left.')
else:
    print(f'Not enough time!{math.floor(diff)} hours needed.')