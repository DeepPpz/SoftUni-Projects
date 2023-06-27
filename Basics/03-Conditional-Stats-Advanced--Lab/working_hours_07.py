hour = int(input())
day = input()

work = False

if 10 <= hour <= 18:
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' \
            or day == 'Friday' or day == 'Saturday':
        work = True
    elif day == 'Sunday':
        work = False

if work:
    print('open')
else:
    print('closed')
