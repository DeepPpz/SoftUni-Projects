first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time + second_time + third_time

minutes = 0
seconds = 0

if total_time < 60:
    seconds += total_time
elif total_time < 120:
    minutes += 1
    seconds += total_time - 60
elif total_time < 180:
    minutes += 2
    seconds += total_time - 120

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')