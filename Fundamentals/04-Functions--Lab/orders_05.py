def orders(product, quantity):
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


product_input = input()
quantity_input = int(input())

order = orders(product_input, quantity_input)
print(f'{order:.2f}')
