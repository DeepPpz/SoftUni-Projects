shirt_price = float(input())
prize_sum = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = (shirt_price + shorts_price) * 2

discount = 0.15

total_price = shirt_price + shorts_price + socks_price + shoes_price
total_price *= 1 - discount

if total_price >= prize_sum:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_price:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {prize_sum - total_price:.2f} lv. more.')
