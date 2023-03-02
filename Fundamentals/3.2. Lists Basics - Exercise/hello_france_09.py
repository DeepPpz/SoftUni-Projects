items = input().split('|')
budget = float(input())

prices = []
profit = 0

for i in range(len(items)):
    curr_item = items[i].split('->')
    buying_price = float(curr_item[1])

    if (curr_item[0] == 'Clothes' and buying_price <= 50) or \
            (curr_item[0] == 'Shoes' and buying_price <= 35) or \
            (curr_item[0] == 'Accessories' and buying_price <= 20.50):
        if budget < buying_price:
            continue
        else:
            budget -= buying_price
            selling_price = buying_price * 1.4
            prices.append(selling_price)
            profit += selling_price - buying_price

print(' '.join('{:0.2f}'.format(i) for i in prices))
print(f'Profit: {profit:.2f}')

if budget + sum(prices) >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')