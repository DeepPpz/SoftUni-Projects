pages = int(input())
pages_hour = int(input())
days = int(input())

time_needed = pages // pages_hour
hours_day = time_needed / days

print(hours_day)