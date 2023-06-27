needed_money = float(input())
owned_money = float(input())

days_count = 0
spend_days = 0
spend_flag = False

while True:
    days_count += 1
    action = input()
    curr_sum = float(input())

    if action == 'spend':
        spend_days += 1
        owned_money -= curr_sum
        if owned_money < 0:
            owned_money = 0
        if spend_days >= 5:
            spend_flag = True
            break
    elif action == 'save':
        spend_days = 0
        owned_money += curr_sum
        if owned_money >= needed_money:
            break

if spend_flag:
    print("You can't save the money.")
    print(f'{days_count}')
else:
    print(f'You saved the money for {days_count} days.')
