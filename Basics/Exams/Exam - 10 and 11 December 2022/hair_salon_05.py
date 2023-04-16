day_target = int(input())

total_profit = 0
goal_flag = False

service_type = input()

while service_type != 'closed':
    if service_type == 'haircut':
        specifics = input()
        if specifics == 'mens':
            total_profit += 15
        elif specifics == 'ladies':
            total_profit += 20
        elif specifics == 'kids':
            total_profit += 10

    elif service_type == 'color':
        specifics = input()
        if specifics == 'touch up':
            total_profit += 20
        elif specifics == 'full color':
            total_profit += 30

    if total_profit >= day_target:
        goal_flag = True
        break

    service_type = input()

if goal_flag:
    print('You have reached your target for the day!')
else:
    print(f'Target not reached! You need {day_target - total_profit}lv. more.')
print(f'Earned money: {total_profit}lv.')