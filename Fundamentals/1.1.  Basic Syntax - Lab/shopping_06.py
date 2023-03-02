budget = int(input())

command = input().lower()

while command != 'end':
    price = int(command)

    if budget < price:
        print('You went in overdraft!')
        exit()
    else:
        budget -= price

    command = input().lower()

print('You bought everything needed.')