n = int(input())

win_weight, win_time, win_quality = 0, 0, 0
max_value = -100000000000000000000000

for balls in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    curr_value = int((weight / time) ** quality)

    if max_value < curr_value:
        win_weight, win_time, win_quality = weight, time, quality
        max_value = curr_value

print(f'{win_weight} : {win_time} = {max_value} ({win_quality})')
