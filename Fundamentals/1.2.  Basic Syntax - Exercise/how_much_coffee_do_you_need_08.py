coffee_counter = 0

while True:
    command = input()

    if command == 'END':
        break
    elif command in ['coding', 'dog', 'cat', 'movie']:
        coffee_counter += 1
    elif command in ['CODING', 'DOG', 'CAT', 'MOVIE']:
        coffee_counter += 2
    else:
        continue

if coffee_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_counter)