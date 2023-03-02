exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrive_time = arrive_hour * 60 + arrive_minute
diff = exam_time - arrive_time

#on time = 30min before
if 0 < diff <= 30:
    print('On time')
    print(f'{diff} minutes before the start')

elif diff == 0:
    print('On time')

#early = more than 30min before
elif diff > 30:
    print('Early')
    if diff < 60:
        print(f'{diff} minutes before the start')
    else:
        print(f'{diff // 60}:{diff % 60:02d} hours before the start')

#late = after start
elif arrive_time > exam_time:
    print('Late')
    if abs(diff) < 60:
        print(f'{abs(diff)} minutes after the start')
    else:
        print(f'{abs(diff) // 60}:{abs(diff) % 60:02d} hours after the start')