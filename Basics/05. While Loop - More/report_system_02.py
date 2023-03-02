required_money = int(input())

rounds = 1
cash_sum = 0
cash_rounds = 0
card_sum = 0
card_rounds = 0
collected_flag = False

while True:
    curr_pay = input()

    if curr_pay == 'End':
        print('Failed to collect required money for charity.')
        break

    curr_pay = float(curr_pay)

    if rounds % 2 == 0: #card
        if curr_pay < 10:
            print('Error in transaction!')
        else:
            card_sum += curr_pay
            card_rounds += 1
            print(f'Product sold!')
    else: #cash
        if curr_pay > 100:
            print('Error in transaction!')
        else:
            cash_sum += curr_pay
            cash_rounds += 1
            print(f'Product sold!')

    if required_money <= cash_sum + card_sum:
        collected_flag = True
        break

    rounds += 1

if collected_flag:
    print(f'Average CS: {cash_sum / cash_rounds:.2f}')
    print(f'Average CC: {card_sum / card_rounds:.2f}')