season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

sport = str
total_price = 0

if season == 'Winter':
    if group_type == 'girls':
        sport = 'Gymnastics'
        total_price = students_count * nights_count * 9.60
    elif group_type == 'boys':
        sport = 'Judo'
        total_price = students_count * nights_count * 9.60
    elif group_type == 'mixed':
        sport = 'Ski'
        total_price = students_count * nights_count * 10.00

elif season == 'Spring':
    if group_type == 'girls':
        sport = 'Athletics'
        total_price = students_count * nights_count * 7.20
    elif group_type == 'boys':
        sport = 'Tennis'
        total_price = students_count * nights_count * 7.20
    elif group_type == 'mixed':
        sport = 'Cycling'
        total_price = students_count * nights_count * 9.50

elif season == 'Summer':
    if group_type == 'girls':
        sport = 'Volleyball'
        total_price = students_count * nights_count * 15.00
    elif group_type == 'boys':
        sport = 'Football'
        total_price = students_count * nights_count * 15.00
    elif group_type == 'mixed':
        sport = 'Swimming'
        total_price = students_count * nights_count * 20.00

if students_count >= 50:
    total_price -= total_price * 0.5
elif students_count >= 20:
    total_price -= total_price * 0.15
elif students_count >= 10:
    total_price -= total_price * 0.05

print(f'{sport} {total_price:.2f} lv.')
