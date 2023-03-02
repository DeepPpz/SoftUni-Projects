def orders(products, quantities):
    total_price = 0
    if product == 'coffee':
        total_price = quantity * 1.50
    elif product == 'water':
        total_price = quantity * 1.00
    elif product == 'coke':
        total_price = quantity * 1.40
    elif product == 'snacks':
        total_price = quantity * 2.00
    return total_price


product = input()
quantity = int(input())

order = orders(product, quantity)
print(f'{order:.2f}')