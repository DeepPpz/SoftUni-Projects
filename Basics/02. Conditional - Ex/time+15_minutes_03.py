input_hours = int(input())
input_minutes = int(input())

conv_minutes = input_hours * 60 + input_minutes
sum_minutes = conv_minutes + 15

hours = sum_minutes // 60
minutes = sum_minutes % 60

if hours > 23:
    hours = hours - 24
    print(f'{hours}:{minutes:02d}')
else:
    print(f'{hours}:{minutes:02d}')