exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrive_time = arrive_hour * 60 + arrive_minute
diff = exam_time - arrive_time
hour = abs(diff) // 60
minutes = abs(diff) % 60

student_arrival = ''
result = ''

if 0 <= diff <= 30:
    student_arrival = 'On time'
    if diff > 0:
        result = f'{minutes} minutes before the start'

elif diff > 30:
    student_arrival = 'Early'

    if diff < 60:
        result = f'{minutes} minutes before the start'
    else:
        result = f'{hour}:{minutes:02d} hours before the start'

elif diff < 0:
    student_arrival = 'Late'

    if abs(diff) < 60:
        result = f'{minutes} minutes after the start'
    else:
        result = f'{hour}:{minutes:02d} hours after the start'

print(student_arrival)
if diff != 0:
    print(result)